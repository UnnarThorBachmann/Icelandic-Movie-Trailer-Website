import webbrowser
import os
import re

""" This file was mostly written in class: Programmings Foundations for Python. However it was modified by Unnar Thor Bachmann to add filtering options
    as well as user experience.
"""
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Icelandic Movies</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
       .thumbnail {
         padding: 1%;
         width: 33.3%;
       }
       .nav-tabs {
         padding: 2%;
       }
       .hidden {
         display: hide;
       }
       h1, h2 {
         padding: 1%;
       }
       img {
         height: 70%;
         width: 90%;
       }
       .container {
         display: flex;
         flex-wrap: wrap;
         flow-direction: row;
       }
       .page-header {
         padding: 3%;
       }
       @media screen and (max-width: 800px) {
        .thumbnail {
          width: 50%;
        }
       }
       @media screen and (max-width: 400px) {
        .thumbnail {
          width: 100%;
        }
       }
    </style>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="page-header">
    <h1>The Icelandic Movie Trailer Website <small>Unnar Thor Bachmann</small></h1>
    <p>This is my solution to the first assignment in Udacity's Full Stack Developers Nanodegree Program. The code was written in the class Programming Foundations for Python
       but modified and enhanced by me. This page contains 56 Icelandic movies, their user rating on <a href="http://www.imdb.com/">IMDB</a>, the plot from <a href="http://www.imdb.com/">IMDB</a>, name of their director,
       and link to their Youtube trailer which opens inside a modal. Part of the code is from class. I added <a href="http://getbootstrap.com/">Bootstrap</a>,
       <a href="https://css-tricks.com/snippets/css/a-guide-to-flexbox/">flexbox</a> and <a href="https://www.python.org/">python</a>code to allow filtering of the set. Many pictures were take from <a href="http://www.kvikmyndavefurinn.is/">kvikmyndavefurinn</a>
       as well as <a href="http://www.imdb.com/">IMDB</a>.
    </p>
    <ul class="nav nav-tabs">
      <li role="presentation" class="active h" id="all"><a href="#">All</a></li>
      <li role="presentation" id="action" class="h"><a href="#">Action</a></li>
      <li role="presentation" id="adventure" class="h"><a href="#">Adventure</a></li>
      <li role="presentation" id="biography" class="h"><a href="#">Biography</a></li>
      <li role="presentation" id="cartoon" class="h"><a href="#">Cartoon</a></li>
      <li role="presentation" id="comedy" class = "h"><a href="#">Comedy</a></li>
      <li role="presentation" id="crime" class="h"><a href="#">Crime</a></li>
      <li role="presentation" id="documentary" class="h"><a href="#">Documentary</a></li>
      <li role="presentation" id="drama" class="h"><a href="#">Drama</a></li>
      <li role="presentation" id="family" class="h"><a href="#">Family</a></li>
      <li role="presentation" id="fantasy" class="h"><a href="#">Fantasy</a></li>
      <li role="presentation" id="history" class="h"><a href="#">History</a></li>
      <li role="presentation" id="horror" class="h"><a href="#">Horror</a></li>
      <li role="presentation" id="new" class="h"><a href="#">New</a></li>
      <li role="presentation" id="romance" class="h"><a href="#">Romance</a></li>
      <li role="presentation" id="sport" class="h"><a href="#">Sport</a></li>
      <li role="presentation" id="thriller" class="h"><a href="#">Thriller</a></li>
      <li role="presentation" class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">
          Release year <span class="caret"></span>
        </a>
        <ul class="dropdown-menu" id="releases">
          {years}
        </ul>
      </li>
      <li role="presentation" class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">
          Directors <span class="caret"></span>
        </a>
        <ul class="dropdown-menu" id="releases">
          {directors}
        </ul>
      </li>
    </ul>
  </div>
  <div class="container">
     {movie_tiles}
  </div>
  <nav>
      <ul class="pager">
        <li id="prev"><a href="#" >Previous</a></li>
        <li id="next"><a href="#">Next</a></li>
      </ul>
  </nav>
'''

""" Unnar Thor Bachmann did split the text file to move the javascript down to the bottom of the html page."""
main_page_cont ='''
     <script type="text/javascript" charset="utf-8">
     var items = 'thumbnail';
     var offset = 0;
     var year = '';
     var director = '';
     /*
     * A function wich is used to filter the movie tiles displayed.
     * This function is run whenever the navigation filters are selected.
     */
     var filter = function() {
       var filtered_list = [];
       var elements = document.getElementsByClassName('thumbnail');

        if (year === '' && director === '') {
          for (var i = 0; i < elements.length; i++) {
            if (elements[i].classList.contains(items)) {
              filtered_list.push(elements[i])
            }
          }
        }
        else if (year === '' && director != '') {
          for (var i = 0; i < elements.length; i++) {
            if (elements[i].classList.contains(director) && elements[i].classList.contains(items)) {
              filtered_list.push(elements[i])
            }
          }
        }
        else if (year != '' && director === '') {
          for (var i = 0; i < elements.length; i++) {
            if (elements[i].classList.contains(year) && elements[i].classList.contains(items)) {
              filtered_list.push(elements[i])
            }
          }
        }
        else {
          for (var i = 0; i < elements.length; i++) {
            if (elements[i].classList.contains(year) && elements[i].classList.contains(director) && elements[i].classList.contains(items)) {
              filtered_list.push(elements[i])
            }
          }
        }
        return filtered_list;
     };
     /*
     * This is a helper function which
     * is ran when new filtering option is
     * selected.
     */
     var refresh = function() {
        offset = 0;
        var filt_items = filter();
        var allItems = document.getElementsByClassName('thumbnail');
        for (var j = 0; j < allItems.length; j++) {
          allItems[j].classList.add('hidden');
        }
        for (var j = 0; j < Math.min(6,filt_items.length); j++) {
          filt_items[j].classList.remove('hidden');
        }
        document.getElementById('prev').classList.add('hidden');
        if (filt_items.length-offset <= 6) {
           document.getElementById('next').classList.add('hidden');
        }
        else {
           document.getElementById('next').classList.remove('hidden');
        }
     };
     /*
     * This is an event listener function which allows the user to scroll back
     * when viewing the movie tiles. Only six tiles are displayed on
     * screen.
     */
     document.getElementById('prev').addEventListener('click', function(e) {
       var elements = filter();
       if (offset >= 6) {
          for (var i = offset; i < offset+6; i++) {
            if (elements[i] != null) {
              elements[i].classList.add('hidden');
            }
          }
          offset = offset - 6;
          for (var i = offset; i < offset+6; i++) {
            if (elements[i] != null) {
              elements[i].classList.remove('hidden');
            }
          }
          if (offset === 0) {
            document.getElementById('prev').classList.add('hidden');
          }
          else {
            document.getElementById('prev').classList.remove('hidden');
          }
          if (elements.length-offset > 6) {
            document.getElementById('next').classList.remove('hidden');
          }
          else {
           document.getElementById('next').classList.add('hidden');
          }
         
       }
       
     });
     /*
     * This is an event listener function which allows the user to scroll forward
     * when viewing the movie tiles. Only six tiles are displayed on
     * screen.
     */
     document.getElementById('next').addEventListener('click', function(e) {
       var elements = filter();
       if (elements.length-offset > 6) {
          for (var i = offset; i < offset+6; i++) {
            if (elements[i] != null) {
              elements[i].classList.add('hidden');
            }
          }
          offset = offset + 6;
          for (var i = offset; i < offset+6; i++) {
            if (elements[i] != null) {
              elements[i].classList.remove('hidden');
            }
          }
          if (offset === 0) {
            document.getElementById('prev').classList.add('hidden');
          }
          else {
            document.getElementById('prev').classList.remove('hidden');
          }
          if (elements.length-offset > 6) {
            document.getElementById('next').classList.remove('hidden');
          }
          else {
           document.getElementById('next').classList.add('hidden');
          }
         
       }
     });
     /*
     * Event listener for filtering by years.
     */
     var years = $('.hyear');
     for (var i=0; i < years.length; i++) {
      document.getElementById(years[i].id).addEventListener('click', function(y) {
        return function() {
          year = y;
          refresh();
        }
      }(years[i].id));
     }
     /*
     * Event listener for filtering by directors.
     */
     var directors = $('.hdirector');
     for (var i=0; i < directors.length; i++) {
      document.getElementById(directors[i].id).addEventListener('click', function(d) {
        return function() {
          director = d;
          refresh();
        }
      }(directors[i].id));
     }
     /*
     * Event listener for filtering by movie category.
     */
     var bar = $('.h');
     for (var i = 0; i < bar.length; i++) {
       document.getElementById(bar[i].id).addEventListener('click', function(t) {
        return function() {

        if (bar[t].id === 'all') {
          $('.active').removeClass('active');
          bar[t].className = 'active';
          items = 'thumbnail';
        }
        else {
          $('.active').removeClass('active');
          bar[t].className = 'active';
          items = bar[t].id;
        }
        year = '';
        director = '';
        offset = 0;
        refresh();
          
        }
      }(i));
    }
    /*
    * Javascript written in class.
    */
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          /*
          * Added by Unnar Thor Bachmann to display first six items when page is loaded.
          */
          document.getElementById('prev').classList.add('hidden');
          var filt_items = filter();
          for (var i = offset; i < offset + 6; i++) {
            filt_items[i].classList.remove('hidden');
          }
        });
 
    </script>
  </body>
</html>
'''

""" Movie tile template for adding a movie to the code. Written in class"""
movie_tile_content = '''<div class="hidden thumbnail movie-tile text-center {movie_class}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                          <img src="{poster_image_url}" alt="{movie_title}" height>
                          <div class="caption">
                            <h3>{header_title} ({movie_year})</h3>
                            <p>{movie_storyline}</p>
                            <h4>User Ratings (IMDB): {movie_ratings}</h4>
                            <h4>Director: {movie_director}</h4>
                          </div>
                        </div>'''

""" A template for adding directors and release years for filtering."""
dropdown_tile_year = '''<li>
                         <a href="#" class="hyear" id="{id_year}">{year}</a>
                        </li>'''
dropdown_tile_director = '''<li>
                             <a href="#" class="hdirector" id="{id_director}">{director}</a>
                            </li>'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content=''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        
        content += movie_tile_content.format(
            movie_class=movie.category,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline = movie.storyline,
            header_title = movie.title,
            movie_year = movie.year,
            movie_ratings = movie.rating,
            movie_director = movie.director
        )
        

    return content

def create_dropdown_list_years(movies):
    """ A function which creates the dropdown of release year from the movies array."""
    dropdown = ''
    movies.sort(key=lambda x: x.year, reverse=True)
    y = []
    for movie in movies:
        y.append(movie.year)
    y = list(set(y))
    for x in y:
        dropdown += dropdown_tile_year.format(id_year=x,
                                         year=x)
        
    return dropdown

def create_dropdown_list_directors(movies):
    """ A function which creates the dropdown of directors from the movies array."""
    dropdown = ''
    d = []
    for movie in movies:
        d.append(movie.director)
    d = list(set(d))
    d.sort();
    for x in d:
        temp = x.lower().replace(' ', '_')
        dropdown += dropdown_tile_director.format(id_director=temp,
                                         director=x)
    return dropdown

def open_movies_page(movies):
    """ A function modified by Unnar Thor Bachmann for the add-ons"""
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    directors_list = create_dropdown_list_directors(movies)
    years_list = create_dropdown_list_years(movies)
    movies.sort(key=lambda x: x.rating, reverse=True)
    # Replace the movie tiles placeholder generated content
    content = create_movie_tiles_content(movies)
    rendered_content = main_page_content.format(
        movie_tiles= content,
        years = years_list,
        directors = directors_list)

    
    # Output the file
    output_file.write(main_page_head + rendered_content+main_page_cont)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
