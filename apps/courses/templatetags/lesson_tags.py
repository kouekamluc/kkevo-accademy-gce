"""Rendering helpers for lesson content.

`rich` turns author text into safe HTML: everything is escaped first, then **bold**,
*italic* and blank-line paragraphs are applied. $...$ is left for KaTeX in the browser.
"""

import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")


def _inline(text):
    html = escape(text or "")
    html = _BOLD.sub(r"<strong>\1</strong>", html)
    return _ITALIC.sub(r"<em>\1</em>", html)


@register.filter
def inline(text):
    """Single-line rich text (no paragraphs)."""
    return mark_safe(_inline(text).replace("\n", "<br>"))


@register.filter
def rich(text):
    """Multi-paragraph rich text."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text or "") if p.strip()]
    return mark_safe("".join(f"<p>{_inline(p).replace(chr(10), '<br>')}</p>" for p in paragraphs))


@register.filter
def lines(text):
    return [line.strip() for line in (text or "").splitlines() if line.strip()]


@register.filter
def mmss(seconds):
    seconds = int(seconds or 0)
    return f"{seconds // 60:02d}:{seconds % 60:02d}" if seconds < 3600 else f"{seconds // 3600}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


@register.simple_tag
def polynomial_plot(data, width=560, height=300, pad=34):
    """SVG geometry for a graph block: {'coeffs': [1, -5, 6], 'xmin', 'xmax', 'ymin', 'ymax', 'roots'}."""
    coeffs = [float(c) for c in data.get("coeffs", [])]
    xmin, xmax = float(data.get("xmin", -5)), float(data.get("xmax", 5))
    ymin, ymax = float(data.get("ymin", -5)), float(data.get("ymax", 5))
    if not coeffs or xmax <= xmin or ymax <= ymin:
        return None

    def f(x):
        y = 0.0
        for c in coeffs:
            y = y * x + c
        return y

    sx = lambda x: pad + (x - xmin) / (xmax - xmin) * (width - 2 * pad)  # noqa: E731
    sy = lambda y: height - pad - (y - ymin) / (ymax - ymin) * (height - 2 * pad)  # noqa: E731
    points, steps = [], 160
    for i in range(steps + 1):
        x = xmin + (xmax - xmin) * i / steps
        y = f(x)
        if ymin - (ymax - ymin) <= y <= ymax + (ymax - ymin):
            points.append(f"{sx(x):.1f},{sy(y):.1f}")
    axis_y = sy(0) if ymin <= 0 <= ymax else height - pad
    axis_x = sx(0) if xmin <= 0 <= xmax else pad
    xticks = [{"x": sx(v), "label": v} for v in range(int(xmin) + 1, int(xmax) + 1)]
    yticks = [{"y": sy(v), "label_y": sy(v) + 4, "label": v}
              for v in range(int(ymin) + 1, int(ymax) + 1) if v and v % 2 == 0]
    roots = [{"x": sx(float(r)), "y": sy(0), "label_y": sy(0) - 12, "label": r} for r in data.get("roots", [])]
    return {
        "width": width, "height": height, "points": " ".join(points), "pad": pad,
        "axis_y": axis_y, "axis_x": axis_x, "bottom": height - pad, "right": width - 20,
        "xlabel_y": axis_y + 18, "ylabel_x": axis_x - 10, "label_x": width - 40,
        "plot_w": width - 20 - pad, "plot_h": height - pad - 10,
        "xticks": xticks, "yticks": yticks, "roots": roots,
    }
