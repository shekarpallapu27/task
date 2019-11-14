var app = angular.module('myApp',  []);



app.config(function($interpolateProvider,$httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});





        // app.controller('LoginController', function($scope,$http,$timeout) {
        //                 debugger;
        //                 $scope.login = function(){
        //                     debugger;
        //                     window.location.href="/login/"
        //         }
        // }



       app.controller('StudentController', function($scope,$http,$timeout) {

        $scope.graph_data = function(student_name,student_marks,modelname){
                // debugger
                    if (modelname=='nodata'){
                        data = null
                        var ctx = document.getElementById("chart-area").getContext("2d");
                        myLineChart = new Chart(ctx).Line(data, options);
                    }

                    
                    var randomScalingFactor = function() {
                        return Math.round(Math.random() * 100);
                    };

                    var config = {  
                        type: 'pie',
                        data: {
                            datasets: [{
                                data: student_marks,
                                backgroundColor: [
                                    window.chartColors.red,
                                    window.chartColors.orange,
                                    window.chartColors.yellow,
                                    window.chartColors.green,
                                    window.chartColors.blue,
                                ],
                                label: 'Dataset 1'
                            }],
                            labels: student_name
                        },
                        options: {
                            responsive: true
                        }
                    };


                    if (modelname=='class'){
                        var ctx = document.getElementById('chart-area').getContext('2d');
                        window.myPie = new Chart(ctx, config);
                    }else{
                        myLineChart = new Chart(ctx).Line(data, options);

                    }


                    // window.onload = function() {

                    // };

                    document.getElementById('randomizeData').addEventListener('click', function() {
                        config.data.datasets.forEach(function(dataset) {
                            dataset.data = dataset.data.map(function() {
                                return randomScalingFactor();
                            });
                        });

                        window.myPie.update();
                    });

                    var colorNames = Object.keys(window.chartColors);
                    document.getElementById('addDataset').addEventListener('click', function() {
                        var newDataset = {
                            backgroundColor: [],
                            data: [],
                            label: 'New dataset ' + config.data.datasets.length,
                        };

                        for (var index = 0; index < config.data.labels.length; ++index) {
                            newDataset.data.push(randomScalingFactor());

                            var colorName = colorNames[index % colorNames.length];
                            var newColor = window.chartColors[colorName];
                            newDataset.backgroundColor.push(newColor);
                        }

                        config.data.datasets.push(newDataset);
                        window.myPie.update();
                    });

                    document.getElementById('removeDataset').addEventListener('click', function() {
                        config.data.datasets.splice(0, 1);
                        window.myPie.update();
                    });






        }




















                        $scope.class_data = function(){

                                // debugger

                                                        // ChartController()

                            // $scope.graph_data()


                            $http.get("/class_data/").then(function(response){
                              $scope.sizes = response.data.data
                            });
                        $scope.update = function() {
                                            $http.get("/api/class/"+$scope.selectinformation+"/").then(function(response){
                                                  $scope.class = response.data

                                                      var student_name = [];
                                                      var student_marks = [];
                                                        var i;
                                                        for (i = 0; i < response.data.length; i++) {
                                                          student_name.push(response.data[i].student_name)
                                                          student_marks.push(response.data[i].Total)
                                                        }

                                                        // console.log(student_name,student_marks)

                                                  // debugger


                                                   $scope.graph_data(student_name,student_marks,'class')

                                            });
                                        }
                $scope.class=true
                $scope.student=false
                $scope.year=false
            }



            // $scope.class_data()

            $scope.stude_data = function(){
                $http.get("/student_data/").then(function(response){
                  $scope.sizes = response.data.data
                });
                    $scope.update = function() {
                        $http.get("/api/student/"+$scope.selectinformation+"/").then(function(response){
                            //debugger
                              $scope.student = response.data

                                var student_name = 1
                                var student_marks = 1

                               $scope.graph_data(student_name,student_marks,'nodata')


                        });
                    }
                $scope.class=false
                $scope.student=true
                $scope.year=false
            }

            $scope.year_data = function(){
                $http.get("/year_data/").then(function(response){
                  $scope.sizes = response.data.data
                });
                    $scope.update = function() {
                        $http.get("/api/year/"+$scope.selectinformation+"/").then(function(response){
                                // debugger
                              $scope.year = response.data


                              var student_name = [];
                              var student_marks = [];
                                var i;
                                for (i = 0; i < response.data.length; i++) {
                                  student_name.push(response.data[i].student_name)
                                  student_marks.push(response.data[i].Total)
                                }

                                // console.log(student_name,student_marks)

                          // debugger


                                 $scope.graph_data(student_name,student_marks,'class')







                        });
                    }
                $scope.class=false
                $scope.student=false
                $scope.year=true
            }







            // $scope.tableinfo = function(){

            //     $http.post("/bucket/info/").then(function(response){
            //         $scope.table_data=response.data.data
            //     });

            // }





    });