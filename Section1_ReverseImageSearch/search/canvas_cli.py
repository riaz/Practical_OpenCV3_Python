from canvas import Canvas

if __name__ == '__main__':
    """
    This is the canvas search engine command line program.

    TODO:
        canvas

            Canvas Revese Image Search Command Line Tool v0.1

                     -i   <Path/to/images>   <index.pkl>    Indexes the Images
                     -s   <Path/to/Scape/Config>           Scrapes Image
                     <Any valid image uri>                 Path to a image url, could be remote/local
    """

    uri = "../resources/img/0b237ed0-34b5-11e7-8b1c-c1a3f64fdbde_sean-diddy-combs-1404.jpg"

    c = Canvas()
    results = c.search(uri)

    for result in results:
        print(result)
