<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <title>
        <xsl:value-of select="root/name"/>
      </title>
      <head>
        <style>
          <![CDATA[.thumbnail{float:left width:110px;height:90px;margin:5px;}]]>
          <![CDATA[.head{background-color:cornsilk;width:90%;height:80px;margin-left:auto;margin-right:auto;}]]>
          <![CDATA[.navibar{background-color:cornsilk;width:90%;margin-left:auto;margin-right:auto;}]]>
          <![CDATA[.mainbody{width:90%;margin-left:auto;margin-right:auto;}]]>
          <![CDATA[.center{margin-left:auto;margin-right:auto;}]]>
        </style>
        <xsl:for-each select="root/css/url">
          <link ref="stylesheet" type="text/css">
            <xsl:attribute name="href">
              <xsl:value-of select="current()"/>
            </xsl:attribute>
          </link>
        </xsl:for-each>
        <xsl:for-each select="root/js/url">
          <script type="text/javascript">
            <xsl:attribute name="src">
              <xsl:value-of select="current()"/>
            </xsl:attribute>
          </script>
        </xsl:for-each>
      </head>
      <body>
        <div style="width:100%;margin-bottom:3px;">
          <div class="head">
            <h1 style="padding-left:20px;margin-top:0px;margin-bottom:0px;">head of the website</h1>
          </div>
        </div>
        <div style="width:100%;margin-bottom:3px;">
          <div class="navibar">
            <ul style="border:black solid 1px;padding-left:10px;margin-top:0px;margin-bottom:0px;">
              <xsl:for-each select="root/location/folder">
                <li style="display:inline">
                  <a>
                    <xsl:attribute name="href">
                      <xsl:value-of select="url"/>
                    </xsl:attribute>
                    <xsl:value-of select="name"/>
                  </a>
                </li>
              </xsl:for-each>
            </ul>
          </div>
        </div>
        <div style="width:100%">
          <div class="mainbody">
            <div style="border:black solid 1px;float:left;width:10%;margin-right:5px">
              <ul style="border:black solid 1px;padding-left:10px;">
                <xsl:for-each select="root/folder">
                <li style="display:inline"><a>
                  <xsl:attribute name="href">
                    <xsl:value-of select="url"/>
                  </xsl:attribute>
                  <xsl:value-of select="name"/>
                </a></li>
                </xsl:for-each>
              </ul>
            </div>
            <div style="border:black solid 1px;float:left">
              <xsl:for-each select="root/file">
                <img class="thumbnail">
                  <xsl:attribute name="src">
                    <xsl:value-of select="url"/>
                  </xsl:attribute>
                </img>
              </xsl:for-each>
            </div>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
