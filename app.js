var app = angular.module('myApp', []);

app.controller('MainController', function($scope, $http) {
    $scope.regions = [];
    $scope.details = [];

    // Fetch the regions from the Flask API
    $http.get('/get_regions')
        .then(function(response) {
            $scope.regions = response.data;
        }, function(error) {
            console.error('Error fetching regions:', error);
        });

    // Fetch the details when a region is selected
    $scope.fetchDetails = function() {
        if ($scope.selectedRegion) {
            $http.get('/get_details', { params: { region: $scope.selectedRegion } })
                .then(function(response) {
                    $scope.details = response.data;
                    console.log(response.data);
                }, function(error) {
                    console.error('Error fetching details:', error);
                });
        } else {
            $scope.details = [];
        }
    };
});