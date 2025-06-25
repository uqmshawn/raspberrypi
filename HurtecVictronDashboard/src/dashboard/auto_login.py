"""Very small auto-login helper.

This is intentionally simple and only fills the first text and password fields
it can find on the page.  Real deployments should replace this logic with a
more robust implementation tailored to the target sites.
"""

from PyQt5.QtWebEngineWidgets import QWebEngineView


def perform_auto_login(view: QWebEngineView, username: str, password: str) -> None:
    """Fill login fields using JavaScript."""

    js = f"""
    (function() {{
        var u = document.querySelector('input[type="email"], input[type="text"]');
        var p = document.querySelector('input[type="password"]');
        if (u) {{ u.value = '{username}'; }}
        if (p) {{ p.value = '{password}'; }}
        if (u && p) {{
            var form = u.form || p.form;
            if (form) form.submit();
        }}
    }})();
    """

    view.page().runJavaScript(js)
