var app = angular.module('addressbook', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'partials/contact.html',
        controller: contacts
    });
    $routeProvider.otherwise({ redirectTo: '/' });
}]);

app.run(['$rootScope', function($rootScope) { 
    $rootScope.title = 'Address Book';
}]);

app.factory("$auth", function($rootScope, $http, $window) {
    var factory = {
        login: function(){
            var data = {
                'email': 'test@gmail.com',
                'passwd': 'qwerty',
            };
            var response = '';
            $http.post('/api/login', data)
            .success(function(res) {
                delete $rootScope.error;
                $window.sessionStorage.access_token = res.access_token;
                $rootScope.access_token = res.access_token;
            })
            .error(function(res) {
                delete $window.sessionStorage.access_token;
                $rootScope.error = res;
            });
        }
    }
    return factory;  
});

app.factory("$twitter", function($http, $window) {
    var factory = {
        tweets: function(user, cid){
            var promise = $http.get('/api/tweets/' + user).then(function (response) {
                return {cid: cid, tweets: response.data};
            });
            return promise;
        }
    }
    return factory;  
});

app.filter('tel', function () {
    return function (tel) {
        if (!tel) { return ''; }
        var value = tel.toString().trim().replace(/^\+/, '');
        if (value.match(/[^0-9]/)) {
            return tel;
        }
        var country = 1;
        var city = value.slice(0, 3);
        var number = value.slice(3);

        if (country == 1) {
            country = "";
        }
        number = number.slice(0, 3) + '-' + number.slice(3);
        return (country + " (" + city + ") " + number).trim();
    };
});



