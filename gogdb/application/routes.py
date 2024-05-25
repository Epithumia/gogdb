import gogdb.views.index
import gogdb.views.product_list
import gogdb.views.product_info
import gogdb.views.build
import gogdb.views.releasenotes
import gogdb.views.changelog
import gogdb.views.changelog_ext
import gogdb.views.manifest
import gogdb.views.favicon
import gogdb.views.legal
import gogdb.views.meta
import gogdb.views.robots
import gogdb.views.moreinfo
import gogdb.views.charts
import gogdb.views.static
import gogdb.views.version_mismatch
import gogdb.views.dependencies



def add_routes(app):
    app.add_url_rule("/", "index", gogdb.views.index.index)
    app.add_url_rule("/products", "product_list", gogdb.views.product_list.product_list)
    app.add_url_rule("/product/<int:prod_id>", "product_info", gogdb.views.product_info.product_info)
    app.add_url_rule("/product/<int:prod_id>/build/<int:build_id>", "build", gogdb.views.build.build)
    app.add_url_rule("/product/<int:prod_id>/releasenotes", "releasenotes", gogdb.views.releasenotes.releasenotes)
    app.add_url_rule("/changelog", "changelog", gogdb.views.changelog.changelog)
    app.add_url_rule("/changelog-ext", "changelog_ext", gogdb.views.changelog_ext.changelog_ext)
    app.add_url_rule("/changelog.xml", "changelog_atom", gogdb.views.changelog_ext.changelog_atom)
    app.add_url_rule("/manifest/<manifest_id>", "manifest", gogdb.views.manifest.manifest)
    app.add_url_rule("/meta/<meta_id>", "meta", gogdb.views.meta.meta)
    app.add_url_rule("/charts/<int:prod_id>.svg", "charts", gogdb.views.charts.charts)
    app.add_url_rule("/charts/<int:prod_id>-ratings.svg", "rating_charts", gogdb.views.charts.rating_charts)
    app.add_url_rule("/charts/<int:prod_id>-rankings.svg", "rankings_charts", gogdb.views.charts.rankings_charts)
    app.add_url_rule("/user/version_mismatch", "version_mismatch", gogdb.views.version_mismatch.version_mismatch)
    app.add_url_rule("/user/dependencies", "dependencies", gogdb.views.dependencies.dependencies)
    # Static pages
    app.add_url_rule("/static/<path:filename>", "static", gogdb.views.static.static)
    app.add_url_rule("/favicon.ico", "favicon", gogdb.views.favicon.favicon)
    app.add_url_rule("/legal", "legal", gogdb.views.legal.legal)
    app.add_url_rule("/robots.txt", "robots", gogdb.views.robots.robots)
    app.add_url_rule("/moreinfo", "moreinfo", gogdb.views.moreinfo.moreinfo)
