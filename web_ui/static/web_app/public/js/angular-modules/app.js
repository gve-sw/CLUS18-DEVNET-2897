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

    // STEP 9 CODE BELOW

    // STEP 10 CODE BELOW

    // STEP 11 CODE BELOW

    // STEP 12 CODE BELOW

    // STEP 13 CODE BELOW


});
