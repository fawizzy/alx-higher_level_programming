$(function(){
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data, status){
        let movies = data.results
        for (i in movies){
            $("UL#list_movies").append("<li>"+movies[i].title+"</li>")
        }
    });
});