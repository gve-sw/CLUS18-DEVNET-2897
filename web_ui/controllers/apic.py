"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import requests
import json

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))
SNAPSHOT_PATH = DIR_PATH + '/snapshots'
# Disable warnings
requests.packages.urllib3.disable_warnings()


class ApicController:
    # TODO: This are sandbox credentials and are hardcoded for simplicity.
    # TODO: By any means include blank password in your source code.
    username = "admin"
    password = "ciscopsdt"
    url = "https://sandboxapicdc.cisco.com/"
    token = ""

    def __init__(self):
        self.token = self.get_token(self.username, self.password)

    def get_token(self, username, password):
        """
        Returns authentication token
        :param url:
        :param username:
        :param password:
        :return:
        """
        template = JSON_TEMPLATES.get_template('login.j2.json')
        payload = template.render(username=username, password=password)
        auth = self.makeCall(p_url='/api/aaaLogin.json', data=payload, method="POST").json()
        login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
        return login_attributes['token']

    def makeCall(self, p_url, method, data=""):
        """
        Basic method to make a call. Please this one to all the calls that you want to make
        :param p_url: APIC URL
        :param method: POST/GET
        :param data: Payload that you want to send
        :return:
        """
        cookies = {'APIC-Cookie': self.token}
        if method == "POST":
            response = requests.post(self.url + p_url, data=data, cookies=cookies, verify=False)
        elif method == "GET":
            response = requests.get(self.url + p_url, cookies=cookies, verify=False)
        if 199 < response.status_code < 300:
            return response
        else:
            error_message = json.loads(response.text)['imdata'][0]['error']['attributes']['text']
            if error_message.endswith("already exists."):
                return None
            else:
                raise Exception(error_message)

    def getSwitches(self, pod_dn):
        """

        :param pod_dn:
        :return:
        """
        switches = self.makeCall(
            p_url='/api/node/mo/' + pod_dn + '.json?query-target=children&target-subtree-class=fabricNode&query-target-filter=and(ne(fabricNode.role,"controller"))',
            method="GET").json()['imdata']
        return switches

    def getLeafs(self, pod_dn):
        switches = self.makeCall(
            p_url='/api/node/mo/' + pod_dn + '.json?query-target=children&target-subtree-class=fabricNode&query-target-filter=and(eq(fabricNode.role,"leaf"))',
            method="GET").json()['imdata']
        return switches

    def getPods(self):
        pods = self.makeCall(p_url='/api/node/class/fabricPod.json', method="GET").json()['imdata']
        return pods

    def getInterfaces(self, switch_dn):
        interfaces = self.makeCall(
            p_url='/api/node/class/' + switch_dn + '/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf&order-by=l1PhysIf.id',
            method="GET").json()['imdata']
        return interfaces

    def getEPGs(self, ap_dn, query_filter=""):
        query_strings = "?query-target=children&target-subtree-class=fvAEPg&order-by=fvAEPg.name"
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        epgs = self.makeCall(
            p_url='/api/node/mo/' + ap_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return epgs

    def createEPG(self, ap_dn, bridge_domain_name, epg_name):
        template = JSON_TEMPLATES.get_template('add_epg.j2.json')
        payload = template.render(ap_dn=ap_dn,
                                  name=epg_name,
                                  bridge_domain_name=bridge_domain_name)
        self.makeCall(
            p_url='/api/node/mo/' + ap_dn + '/epg-' + epg_name + '.json',
            data=payload,
            method="POST")
        return self.getEPGs(ap_dn=ap_dn,
                            query_filter='eq(fvAEPg.name,"' + epg_name + '")')

    def getTenants(self, query_filter=""):
        query_strings = "?order-by=fvTenant.name|asc"
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        tenants = self.makeCall(
            p_url='/api/node/class/fvTenant.json' + query_strings,
            method="GET").json()['imdata']
        return tenants

    def getAppProfiles(self, tenant_dn, query_filter=""):
        query_strings = '?order-by=fvAp.name|asc&query-target=subtree&target-subtree-class=fvAp'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        aps = self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return aps

    def createTenant(self, tenant_name):
        template = JSON_TEMPLATES.get_template('add_tenant.j2.json')
        payload = template.render(name=tenant_name)
        self.makeCall(
            p_url='/api/node/mo/uni/tn-' + tenant_name + '.json',
            data=payload,
            method="POST")
        return self.getTenants(query_filter='eq(fvTenant.name,"' + tenant_name + '")')

    def createAppProfile(self, tenant_dn, app_prof_name):
        template = JSON_TEMPLATES.get_template('add_app_profile.j2.json')
        payload = template.render(tenant_dn=tenant_dn, ap_name=app_prof_name)
        self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '/ap-' + app_prof_name + '.json',
            data=payload,
            method="POST")
        return self.getAppProfiles(tenant_dn=tenant_dn,
                                   query_filter='eq(fvAp.name,"' + app_prof_name + '")')

    def getVRFs(self, tenant_dn, query_filter=""):
        query_strings = '?query-target=children&target-subtree-class=fvCtx&order-by=fvCtx.name|asc'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        vrfs = self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return vrfs

    def createVRF(self, tenant_dn, vrf_name):
        template = JSON_TEMPLATES.get_template('add_vrf.j2.json')
        payload = template.render(tenant_dn=tenant_dn, name=vrf_name)
        self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '/ctx-' + vrf_name + '.json',
            data=payload,
            method="POST")
        return self.getVRFs(tenant_dn=tenant_dn,
                            query_filter='eq(fvCtx.name,"' + vrf_name + '")')

    def getBridgeDomains(self, tenant_dn, query_filter=""):
        query_strings = '?query-target=children&target-subtree-class=fvBD&order-by=fvBD.name|asc'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        bds = self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return bds

    def createBridgeDomain(self, tenant_dn, bd_name, vrf_name, unk_mac_uni_action="flood", arp_flood="true"):
        template = JSON_TEMPLATES.get_template('add_bridge_domain.j2.json')
        payload = template.render(tenant_dn=tenant_dn, name=bd_name,
                                  unk_mac_uni_action=unk_mac_uni_action,
                                  arp_flood=arp_flood,
                                  vrf_name=vrf_name)
        self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '/BD-' + bd_name + '.json',
            data=payload,
            method="POST")
        return self.getBridgeDomains(tenant_dn=tenant_dn,
                                     query_filter='eq(fvBD.name,"' + bd_name + '")')

    def getVlanPools(self, query_filter=""):
        query_strings = '?query-target=children&target-subtree-class=fvnsVlanInstP'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        vPools = self.makeCall(
            p_url='/api/node/mo/uni/infra.json' + query_strings,
            method="GET").json()['imdata']
        return vPools

    def createVlanPool(self, name, allocation_mode="static"):
        template = JSON_TEMPLATES.get_template('add_vlan_pool.j2.json')
        payload = template.render(name=name,
                                  allocation_mode=allocation_mode)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/vlanns-[' + name + ']-' + allocation_mode + '.json',
            data=payload,
            method="POST")
        return self.getVlanPools(query_filter='eq(fvnsVlanInstP.name,"' + name + '")')

    def addVlansToPool(self, pool_name, from_vlan, to_vlan):
        template = JSON_TEMPLATES.get_template('add_vlans_to_pool.j2.json')
        payload = template.render(pool_name=pool_name,
                                  from_vlan=from_vlan,
                                  to_vlan=to_vlan)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/vlanns-[' + pool_name + ']-static/from-[vlan-' + from_vlan + ']-to-[vlan-' + to_vlan + '].json',
            data=payload,
            method="POST")

    def createPhysicalDomain(self, name, vlan_pool_dn):
        template = JSON_TEMPLATES.get_template('add_physical_domain.j2.json')
        payload = template.render(name=name,
                                  vlan_pool_dn=vlan_pool_dn)
        self.makeCall(
            p_url='/api/node/mo/uni/phys-' + name + '.json',
            data=payload,
            method="POST")
        return self.getPhysicalDomains(query_filter='eq(physDomP.name,"' + name + '")')

    def getPhysicalDomains(self, query_filter=""):
        query_strings = '?'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        phyDoms = self.makeCall(
            p_url='/api/node/class/physDomP.json' + query_strings,
            method="GET").json()['imdata']
        return phyDoms

    def createAttachEntityProfile(self, name, phy_domain_dn):
        template = JSON_TEMPLATES.get_template('add_attach_entity_profile.j2.json')
        payload = template.render(name=name,
                                  phy_domain_dn=phy_domain_dn)
        self.makeCall(
            p_url='/api/node/mo/uni/infra.json',
            data=payload,
            method="POST")
        return self.getAttachEntityProfile(query_filter='eq(infraAttEntityP.name,"' + name + '")')

    def getAttachEntityProfile(self, query_filter=""):
        query_strings = '?query-target=children&target-subtree-class=infraAttEntityP'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        attEntProfs = self.makeCall(
            p_url='/api/node/mo/uni/infra.json' + query_strings,
            method="GET").json()['imdata']
        return attEntProfs

    def createAccessInterfacePolicyGroup(self, name, attEntPro_dn):
        template = JSON_TEMPLATES.get_template('add_access_interface_policy_group.j2.json')
        payload = template.render(name=name,
                                  atth_ent_prof_dn=attEntPro_dn)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/funcprof/accportgrp-' + name + '.json',
            data=payload,
            method="POST")
        return [json.loads(payload)]

    def getAccessInterfacePolicyGroup(self, query_filter=""):
        query_strings = ''
        if query_filter != '':
            query_strings += '?query-target-filter=' + query_filter
        accIntPolGroups = self.makeCall(
            p_url='/api/node/class/infraAccBaseGrp.json' + query_strings,
            method="GET").json()['imdata']
        return accIntPolGroups

    def createAccessInterfaceProfile(self, name):
        template = JSON_TEMPLATES.get_template('add_access_interface_profile.j2.json')
        payload = template.render(name=name)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/accportprof-' + name + '.json',
            data=payload,
            method="POST")
        return [json.loads(payload)]

    def getAccessInterfaceProfiles(self, query_filter=""):
        query_strings = '?target-subtree-class=infraFexP,infraAccPortP&query-target=subtree'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        accInterProfs = self.makeCall(
            p_url='/api/node/mo/uni/infra.json' + query_strings,
            method="GET").json()['imdata']
        return accInterProfs

    def createInterfaceSelector(self, name, from_port, to_port, interface_profile_dn, interface_policy_group_dn):
        template = JSON_TEMPLATES.get_template('add_interface_selector_to_profile.j2.json')
        payload = template.render(name=name,
                                  from_port=from_port,
                                  to_port=to_port,
                                  interface_profile_dn=interface_profile_dn,
                                  interface_policy_group_dn=interface_policy_group_dn)
        self.makeCall(
            p_url='/api/node/mo/' + interface_profile_dn + '/hports-' + name + '-typ-range.json',
            data=payload,
            method="POST")

    def createSwitchProfile(self, name, leaf_id):
        template = JSON_TEMPLATES.get_template('add_switch_profile.j2.json')
        payload = template.render(name=name,
                                  leaf_id=leaf_id)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/nprof-' + name + '-' + leaf_id + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def associateIntProfToSwProf(self, sw_prof_dn, int_prof_dn):
        template = JSON_TEMPLATES.get_template('asociate_int_prof_to_sw_prof.j2.json')

        payload = template.render(int_prof_dn=int_prof_dn)
        self.makeCall(
            p_url='/api/node/mo/' + sw_prof_dn + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def addStaticPortToEpg(self, vlan, leaf_id, port_id, epg_dn):
        template = JSON_TEMPLATES.get_template('add_static_port_to_epg.j2.json')

        payload = template.render(vlan=vlan,
                                  leaf_id=leaf_id,
                                  port_id=port_id)
        self.makeCall(
            p_url='/api/node/mo/' + epg_dn + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def addLacpProf(self, name):
        template = JSON_TEMPLATES.get_template('add_lacp_profile.j2.json')

        payload = template.render(name=name)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/lacplagp-' + name + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def addPortchannelIntPolicyGroup(self, name, att_ent_prof_dn, lacp_prof_name):
        template = JSON_TEMPLATES.get_template('add_portchannel_interface_policy_group.j2.json')

        payload = template.render(name=name,
                                  att_ent_prof_dn=att_ent_prof_dn,
                                  lacp_prof_name=lacp_prof_name)
        self.makeCall(
            p_url='/api/node/mo/uni/infra/funcprof/accbundle-' + name + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def addPortchannelIntProfile(self, name):
        template = JSON_TEMPLATES.get_template('add_portchan_inter_prof.j2.json')

        payload = template.render(name=name)
        self.makeCall(
            p_url='api/node/mo/uni/infra/accportprof-' + name + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def addStaticPortchannelToEpg(self, vlan, leaf_id, portchannel_pol_grp_name, epg_dn):
        template = JSON_TEMPLATES.get_template('add_static_portchannel.j2.json')

        payload = template.render(vlan=vlan,
                                  leaf_id=leaf_id,
                                  portchannel_pol_grp_name=portchannel_pol_grp_name)
        self.makeCall(
            p_url='api/node/mo/' + epg_dn + '.json',
            data=payload,
            method="POST")
        return json.loads(payload)

    def createDeployment(self, payload, prefix):
        print("Creating tenant if not present")
        tenants = self.getTenants(query_filter='eq(fvTenant.name,"' + prefix + '")')
        if len(tenants) == 0:
            tenants = self.createTenant(prefix)

        print("Creating application profile if not present")
        aps = self.getAppProfiles(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                  query_filter='eq(fvAp.name,"' + prefix + '")')
        if len(aps) == 0:
            aps = self.createAppProfile(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                        app_prof_name=prefix)

        print("Creating VRF if not present")
        vrfs = self.getVRFs(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                            query_filter='eq(fvCtx.name,"' + prefix + '")')

        if len(vrfs) == 0:
            vrfs = self.createVRF(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                  vrf_name=prefix)

        print("Creating Bridge Domain if not present")
        bds = self.getBridgeDomains(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                    query_filter='eq(fvBD.name,"' + prefix + '")')

        if len(bds) == 0:
            bds = self.createBridgeDomain(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                          bd_name=prefix,
                                          vrf_name=vrfs[0]["fvCtx"]["attributes"]["name"])

        print("Creating Endpoint Group if not present")
        if payload["deployment"]["epgAction"] == "new":
            epgName = payload["deployment"]["selectedEpg"]
        else:
            epgName = payload["deployment"]["selectedEpg"]["fvAEPg"]["attributes"]["name"]

        # Check if EPG already exists
        epgs = self.getEPGs(ap_dn=aps[0]["fvAp"]["attributes"]["dn"],
                            query_filter='eq(fvAEPg.name,"' + epgName + '")')
        if len(epgs) == 0:
            # Create only if does not exist
            epgs = self.createEPG(ap_dn=aps[0]["fvAp"]["attributes"]["dn"],
                                  bridge_domain_name=bds[0]["fvBD"]["attributes"]["name"],
                                  epg_name=epgName)

        print("Creating VLAN Pool if not present")
        vpools = self.getVlanPools(query_filter='eq(fvnsVlanInstP.name,"' + prefix + '")')

        if len(vpools) == 0:
            # Create vlan pool
            vpools = self.createVlanPool(name=prefix)

        print("Add selected VLANs to pool if not present")
        self.addVlansToPool(pool_name=vpools[0]["fvnsVlanInstP"]["attributes"]["name"],
                            from_vlan=epgName, to_vlan=epgName)

        print("Creating Physical Domain if not present")
        phyDoms = self.getPhysicalDomains(query_filter='eq(physDomP.name,"' + prefix + '")')
        if len(phyDoms) == 0:
            phyDoms = self.createPhysicalDomain(name=prefix,
                                                vlan_pool_dn=vpools[0]["fvnsVlanInstP"]["attributes"]["dn"])

        print("Creating Attachable Entity Profile if not present")
        atthEntProfiles = self.getAttachEntityProfile(query_filter='eq(infraAttEntityP.name,"' + prefix + '")')
        if len(atthEntProfiles) == 0:
            atthEntProfiles = self.createAttachEntityProfile(name=prefix,
                                                             phy_domain_dn=phyDoms[0]["physDomP"]["attributes"][
                                                                 "dn"])
        port1 = payload["deployment"]["selectedPort1"]["l1PhysIf"]["attributes"]["id"].replace(
            "eth1/", "")

        leaf1_id = payload["deployment"]["selectedSwitch"]["fabricNode"]["attributes"]["id"]

        if payload["deployment"]["portType"] == "access":
            # ## Access ##
            # Create Policy Group default options with attachable entity profile
            print("**** Deployment Port Type: Individual *****")
            intPolGroups = self.createAccessInterfacePolicyGroup(
                name=prefix + "-access",
                attEntPro_dn=atthEntProfiles[0]["infraAttEntityP"]["attributes"]["dn"])

            print("Creating Interface Policy if not present")
            # Create access interface policy
            intAccessProfiles = self.createAccessInterfaceProfile(name=prefix + "-access-" + port1)

            print("Creating Interface Selector if not present")
            # Add selected port
            self.createInterfaceSelector(
                name=payload["deployment"]["selectedPort1"]["l1PhysIf"]["attributes"]["id"].replace(
                    "/", "-"),
                from_port=port1,
                to_port=port1,
                interface_profile_dn=intAccessProfiles[0]["infraAccPortP"]["attributes"]["dn"],
                interface_policy_group_dn=intPolGroups[0]["infraAccPortGrp"]["attributes"]["dn"])

            print("Creating Switch Profile if not present")
            # Create switch profile
            sProfile = self.createSwitchProfile(name=prefix, leaf_id=leaf1_id)

            print("Associating interface profiles to switch profile if not present")
            # Associate interface profiles to switch profile sw_prof_dn, int_prof_dn
            self.associateIntProfToSwProf(
                sw_prof_dn=sProfile["infraNodeP"]["attributes"]["dn"],
                int_prof_dn=intAccessProfiles[0]["infraAccPortP"]["attributes"]["dn"])

            print("Associating port to EPG if not present")
            # Associate port to EPG
            self.addStaticPortToEpg(
                vlan=epgName,
                leaf_id=leaf1_id,
                port_id=payload["deployment"]["selectedPort1"]["l1PhysIf"]["attributes"]["id"],
                epg_dn=epgs[0]["fvAEPg"]["attributes"]["dn"])

        elif payload["deployment"]["portType"] == "portChannel":

            print("**** Deployment Port Type: PortChannel *****")
            # ## Port Channel ##
            port2 = payload["deployment"]["selectedPort2"]["l1PhysIf"]["attributes"]["id"].replace(
                "eth1/", "")

            print("Creating LACP Profile if not present")
            # make sure lacp_profile exists
            lapc_prof = self.addLacpProf(name=prefix + '-LACP-ACTIVE')

            print("Creating port channel policy group if not present")
            # make sure portchannel policy group exists
            portchannel_policy = self.addPortchannelIntPolicyGroup(
                name=prefix + '-portchannel',
                att_ent_prof_dn=atthEntProfiles[0]["infraAttEntityP"]["attributes"]["dn"],
                lacp_prof_name=lapc_prof["lacpLagPol"]["attributes"]["name"])

            print("Creating port channel profile if not present")
            # make sure portchannel profile exists for port 1
            portchannel_profile = self.addPortchannelIntProfile(
                name=prefix + '-portchannel-' + port1 + '-' + port2)

            print("Creating Interface Selector for interfaces if not present")
            # Add selected port1
            self.createInterfaceSelector(
                name=payload["deployment"]["selectedPort1"]["l1PhysIf"]["attributes"]["id"].replace(
                    "/", "-"),
                from_port=port1,
                to_port=port1,
                interface_profile_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"],
                interface_policy_group_dn=portchannel_policy["infraAccBndlGrp"]["attributes"]["dn"])

            # Add selected port2
            self.createInterfaceSelector(
                name=payload["deployment"]["selectedPort2"]["l1PhysIf"]["attributes"]["id"].replace(
                    "/", "-"),
                from_port=port2,
                to_port=port2,
                interface_profile_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"],
                interface_policy_group_dn=portchannel_policy["infraAccBndlGrp"]["attributes"]["dn"])

            print("Creating Switch Profile if not present")
            # Create switch Profile
            sProfile = self.createSwitchProfile(name=prefix, leaf_id=leaf1_id)

            print("Associating interface profiles to switch profile if not present")
            # Associate interface profiles to switch profile sw_prof_dn, int_prof_dn
            self.associateIntProfToSwProf(
                sw_prof_dn=sProfile["infraNodeP"]["attributes"]["dn"],
                int_prof_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"])

            print("Associating port to EPG if not present")
            # Associate port to EPG
            self.addStaticPortchannelToEpg(
                vlan=epgName,
                leaf_id=leaf1_id,
                portchannel_pol_grp_name=portchannel_policy["infraAccBndlGrp"]["attributes"]["name"],
                epg_dn=epgs[0]["fvAEPg"]["attributes"]["dn"])
