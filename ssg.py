import typer
from ssg.site import Site

def main(source = 'content',dest = 'dist'):
    config = {}
    config["source"]=source
    config["dest"]=dest
    Site(source,dest).build()
typer.run(main())