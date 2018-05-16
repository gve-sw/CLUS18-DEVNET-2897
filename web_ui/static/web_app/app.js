/**
 * Angular JavaScript that controls the user interface interactions .
 * @module App module
 * @author Santiago Flores Kanter <sfloresk@cisco.com>
 * @copyright Copyright (c) 2018 Cisco and/or its affiliates.
 * @license Cisco Sample Code License, Version 1.0
 */

/**
 * @license
 * Copyright (c) 2018 Cisco and/or its affiliates.
 *
 * This software is licensed to you under the terms of the Cisco Sample
 * Code License, Version 1.0 (the "License"). You may obtain a copy of the
 * License at
 *
 *                https://developer.cisco.com/docs/licenses
 *
 * All use of the material herein must be in accordance with the terms of
 * the License. All rights not expressly granted by the License are
 * reserved. Unless required by applicable law or agreed to separately in
 * writing, software distributed under the License is distributed on an "AS
 * IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */
var appModule = angular.module('appModule',['ngRoute','ngAnimate'])

/*  Configuration    */

// Application routing
appModule.config(function($routeProvider, $locationProvider){
    // Maps the URLs to the templates located in the server
    $routeProvider
        .when('/', {templateUrl: 'ng/home'})
        .when('/home', {templateUrl: 'ng/home'})

    $locationProvider.html5Mode(true);
});

// To avoid conflicts with other template tools such as Jinja2, all between {a a} will be managed by Angular instead of {{ }}
appModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);


/*  Controllers    */

// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope){

    // Variables initialization
    $scope.error = "";
    $scope.success = "";
    $scope.loading = false;
    $scope.pods = [];
    $scope.deployment={selectedPod: ""};
    $scope.deployment.portType = "access";
    $scope.deployment.epgAction = "existing";


    // Functions
    $scope.go = function ( path ) {
        $location.path( path );
    };

    $scope.clearError = function(){
        $scope.error = "";
    };

    $scope.clearSuccess = function(){
        $scope.success = "";
    };

    $scope.setPortType = function(portType){
        $scope.deployment.portType = portType;
    };


    $scope.setEpgAction = function(epgAction){
        $scope.deployment.epgAction = epgAction;
    };

    // STEP 8 CODE BELOW

    // STEP 9 CODE BELOW

    // STEP 10 CODE BELOW

    // STEP 11 CODE BELOW

    // STEP 12 CODE BELOW


});
