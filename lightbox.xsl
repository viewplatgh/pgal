<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"&gt;</xsl:text>
    <xsl:variable name="empty" select="' '"/>
    <html>
      <head>
        <title>
          <xsl:value-of select="root/name"/>
        </title>
        <xsl:for-each select="root/js/url">
          <script type="text/javascript">
            <xsl:attribute name="src">
              <xsl:value-of select="."/>
            </xsl:attribute>
            <xsl:value-of select="$empty"/>
          </script>
        </xsl:for-each>
        <xsl:for-each select="root/css/url">
          <link rel="stylesheet" type="text/css">
            <xsl:attribute name="href">
              <xsl:value-of select="."/>
            </xsl:attribute>
          </link>
        </xsl:for-each>
        <style>
          <![CDATA[
        h1, h2
        {
            border: rgb(0, 0, 0) 2px solid;
            border-left: 1px none;
            border-right: 1px none;
            border-top: 1px none;
            margin-bottom: 1em;
            margin-left: -10px;
            margin-right: 0px;
            padding: 20px;
            width: 98%;
            display: block;
            color: rgb(0, 0, 0);
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 4px;
            text-align: right;
            height: 21px;
            position: relative;
        }
        h2:first-letter
        {
            color: rgb(0, 0, 0);
            font-weight: bold;
            font-size: 24pt;
        }
        a, a:link, a:visited, a:active
        {
            color: rgb(0, 0, 0);
            text-decoration: none;
        }
        a:hover
        {
            color: rgb(255, 0, 0);
            text-decoration: none;
        }
        body
        {
            font-family: Verdana, sans-serif;
            font-size: larger;
            margin-bottom: 20px;
            margin-top: 0px;
            color: rgb(0, 0, 0);
            background: rgb(153, 102, 51);
        }
        td
        {
            text-align: center;
        }
        img
        {
            border-style: solid;
            border-color: rgb(0,0,0);
            border-width: 0px;
        }
        table.center
        {
            margin-left: auto;
            margin-right: auto;
        }
        #httphotos
        {
            position: absolute;
            right: 0px;
            bottom: 20px;
            margin: 0px;
            padding: 0px;
        }
        
        #httphotos img
        {
            border: 0px;
        }]]>
        </style>
      </head>
      <body>
        <h2>
          <xsl:value-of select="root/name"/>
        </h2>
        <div>
          <xsl:for-each select="root/location/folder">
            <a>
              <xsl:attribute name="href">
                <xsl:value-of select="url"/>
              </xsl:attribute>
              <xsl:value-of select="name"/>
            </a>
            <xsl:choose>
              <xsl:when test="position() != last()"> &gt;&gt; </xsl:when>
            </xsl:choose>
          </xsl:for-each>
        </div>
        <div>
          <table class="center">
              <tbody>
                <xsl:apply-templates select="root/file[position() mod 5 = 1]"/>
              </tbody>
          </table>
        </div>
      </body>
    </html>
  </xsl:template>
  <xsl:template match="file">
    <tr>
      <xsl:apply-templates select="self::*|following-sibling::file[position() &lt; 5]" mode="cell" />
    </tr>
  </xsl:template>
  <xsl:template match="file" mode="cell">
    <td>
      <a rel="lightbox-cats" title="">
        <xsl:attribute name="href">
          <xsl:value-of select="concat('./', name)"/>
        </xsl:attribute>
        <img alt="Click!">
          <xsl:attribute name="src">
            <xsl:value-of select="concat('./', name)"/>
          </xsl:attribute>
        </img>
      </a>
    </td>
  </xsl:template>
</xsl:stylesheet>