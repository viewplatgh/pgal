<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <style>
          <![CDATA[ui{list-style-type:none;}.thumbnail{float:left width:110px;height:90px;margin:5px;}]]>
        </style>
      </head>
      <body>
        <div style="float:left" width="10%">
          <ul>
            <xsl:for-each select="root/folder">
            <li><a>
              <xsl:attribute name="href">
                <xsl:value-of select="concat('./', name)"/>
              </xsl:attribute>
              <xsl:value-of select="name"></xsl:value-of>
            </a></li>
            </xsl:for-each>
          </ul>
        </div>
        <div style="float:left">
          <xsl:for-each select="root/file">
            <img class="thumbnail">
              <xsl:attribute name="src">
                <xsl:value-of select="concat('./', name)"></xsl:value-of>
              </xsl:attribute>
            </img>
          </xsl:for-each>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>