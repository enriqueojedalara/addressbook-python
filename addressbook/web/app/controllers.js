function contacts($rootScope, $scope, $http, $auth, $twitter, $window) {
    $scope.tweets = $rootScope.tweets;
    $scope.twitter = {};
    if (!$window.sessionStorage.access_token){
        $auth.login();
    }
    $http.defaults.headers.common.Authorization = $window.sessionStorage.access_token;
    var promise = $http.get('/api/contacts');
    promise.then(
        function(res){ 
            $scope.contacts = res.data;
            for(i in $scope.contacts){
                for(j in $scope.contacts[i].details.sn)
                    if ($scope.contacts[i].details.sn[j].snid == $rootScope.TWITTER){
                        var user = $scope.contacts[i].details.sn[j].username
                        $twitter.tweets(user, $scope.contacts[i].cid).then(function(d) {
                            $scope.twitter[d.cid] = d.tweets;
                        });  
                    }
            }
        },
        function(error){ 
            $scope.error = error; 
        }
    );
};

function tweets($rootScope, $scope, $http, $auth, $window) {
    var promise = $http.get('/api/tweets');
    promise.then(
        function(res){ 
            $scope.contacts = res.data; 
        },
        function(error){ 
            $scope.error = error; 
        }
    );
};
