from ttfquery import describe, glyphquery, glyph


# Set font here ----->
f = describe.openFont("/Library/Fonts/Impact.ttf")

# Set character here, in this case its C
n = glyphquery.glyphName(f, 'C')
g = glyph.Glyph(n)
c = g.calculateContours(f)
o = glyph.decomposeOutline(c[1])

# Print out the Polyline
print o