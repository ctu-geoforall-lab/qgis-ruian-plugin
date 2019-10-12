<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyDrawingHints="0" simplifyLocal="1" simplifyMaxScale="1" maxScale="0" minScale="1e+08" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" labelsEnabled="1" readOnly="0" version="3.4.12-Madeira" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" symbollevels="0" forceraster="0" enableorderby="0">
    <symbols>
      <symbol type="marker" clip_to_extent="1" alpha="1" force_rhr="0" name="0">
        <layer pass="0" class="SimpleMarker" enabled="1" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="180,180,180,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="1"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style multilineHeight="1" textColor="0,0,0,255" fontWeight="50" fontStrikeout="0" textOpacity="1" previewBkgrdColor="#ffffff" fontFamily="Cantarell" fontSize="10" fieldName="CASE WHEN &quot;cisloorientacni&quot; IS NOT NULL THEN &quot;cislodomovni&quot;  || '/' || &quot;cisloorientacni&quot; ELSE  &quot;cislodomovni&quot; END" namedStyle="Regular" fontUnderline="0" fontWordSpacing="0" fontSizeUnit="Point" fontCapitals="0" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" fontItalic="0" isExpression="1" blendMode="0">
        <text-buffer bufferColor="255,255,255,255" bufferNoFill="1" bufferOpacity="1" bufferDraw="0" bufferJoinStyle="128" bufferBlendMode="0" bufferSizeUnits="MM" bufferSize="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <background shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeDraw="0" shapeRotationType="0" shapeOpacity="1" shapeRotation="0" shapeJoinStyle="64" shapeRadiiY="0" shapeSizeY="0" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeOffsetUnit="MM" shapeRadiiUnit="MM" shapeFillColor="255,255,255,255" shapeOffsetX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetY="0" shapeBorderWidthUnit="MM" shapeSizeType="0" shapeBorderColor="128,128,128,255" shapeRadiiX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeBorderWidth="0"/>
        <shadow shadowOffsetGlobal="1" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowOpacity="0.7" shadowDraw="0" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowBlendMode="6" shadowScale="100" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
        <substitutions/>
      </text-style>
      <text-format decimals="3" multilineAlign="3" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" plussign="0" rightDirectionSymbol=">" placeDirectionSymbol="0" autoWrapLength="0" wrapChar="" addDirectionSymbol="0" formatNumbers="0"/>
      <placement xOffset="0" yOffset="0" fitInPolygonOnly="0" priority="5" centroidWhole="0" placementFlags="10" centroidInside="0" quadOffset="4" maxCurvedCharAngleOut="-25" distUnits="MM" rotationAngle="0" offsetUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" dist="0" distMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" repeatDistanceUnits="MM" placement="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" repeatDistance="0"/>
      <rendering scaleVisibility="1" zIndex="0" fontMinPixelSize="3" mergeLines="0" displayAll="0" scaleMin="0" limitNumLabels="0" drawLabels="1" scaleMax="1000" upsidedownLabels="0" obstacleType="0" obstacle="1" minFeatureSize="0" fontLimitPixelSize="0" maxNumLabels="2000" fontMaxPixelSize="10000" labelPerPart="0" obstacleFactor="1"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" value="" name="name"/>
          <Option name="properties"/>
          <Option type="QString" value="collection" name="type"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minimumSize="0" opacity="1" sizeType="MM" height="15" diagramOrientation="Up" penAlpha="255" barWidth="5" lineSizeType="MM" penColor="#000000" maxScaleDenominator="1e+08" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" minScaleDenominator="-2.14748e+09" enabled="0" sizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" penWidth="0" scaleDependency="Area" rotationOffset="270" width="15" backgroundAlpha="255" labelPlacementMethod="XHeight">
      <fontProperties description="Cantarell,11,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" linePlacementFlags="2" showAll="1" dist="0" zIndex="0" obstacle="0" priority="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="ogc_fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gml_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="kod">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nespravny">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="cislodomovni">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="cisloorientacni">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="cisloorientacnipismeno">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="psc">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="stavebniobjektkod">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ulicekod">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="platiod">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="platido">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="idtransakce">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="globalniidnavrhuzmeny">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="isknbudovaid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="ogc_fid" index="0" name=""/>
    <alias field="gml_id" index="1" name=""/>
    <alias field="kod" index="2" name=""/>
    <alias field="nespravny" index="3" name=""/>
    <alias field="cislodomovni" index="4" name=""/>
    <alias field="cisloorientacni" index="5" name=""/>
    <alias field="cisloorientacnipismeno" index="6" name=""/>
    <alias field="psc" index="7" name=""/>
    <alias field="stavebniobjektkod" index="8" name=""/>
    <alias field="ulicekod" index="9" name=""/>
    <alias field="platiod" index="10" name=""/>
    <alias field="platido" index="11" name=""/>
    <alias field="idtransakce" index="12" name=""/>
    <alias field="globalniidnavrhuzmeny" index="13" name=""/>
    <alias field="isknbudovaid" index="14" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="ogc_fid" expression="" applyOnUpdate="0"/>
    <default field="gml_id" expression="" applyOnUpdate="0"/>
    <default field="kod" expression="" applyOnUpdate="0"/>
    <default field="nespravny" expression="" applyOnUpdate="0"/>
    <default field="cislodomovni" expression="" applyOnUpdate="0"/>
    <default field="cisloorientacni" expression="" applyOnUpdate="0"/>
    <default field="cisloorientacnipismeno" expression="" applyOnUpdate="0"/>
    <default field="psc" expression="" applyOnUpdate="0"/>
    <default field="stavebniobjektkod" expression="" applyOnUpdate="0"/>
    <default field="ulicekod" expression="" applyOnUpdate="0"/>
    <default field="platiod" expression="" applyOnUpdate="0"/>
    <default field="platido" expression="" applyOnUpdate="0"/>
    <default field="idtransakce" expression="" applyOnUpdate="0"/>
    <default field="globalniidnavrhuzmeny" expression="" applyOnUpdate="0"/>
    <default field="isknbudovaid" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="ogc_fid" exp_strength="0" notnull_strength="1" constraints="3" unique_strength="1"/>
    <constraint field="gml_id" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="kod" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="nespravny" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="cislodomovni" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="cisloorientacni" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="cisloorientacnipismeno" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="psc" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="stavebniobjektkod" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="ulicekod" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="platiod" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="platido" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="idtransakce" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="globalniidnavrhuzmeny" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
    <constraint field="isknbudovaid" exp_strength="0" notnull_strength="0" constraints="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ogc_fid" exp="" desc=""/>
    <constraint field="gml_id" exp="" desc=""/>
    <constraint field="kod" exp="" desc=""/>
    <constraint field="nespravny" exp="" desc=""/>
    <constraint field="cislodomovni" exp="" desc=""/>
    <constraint field="cisloorientacni" exp="" desc=""/>
    <constraint field="cisloorientacnipismeno" exp="" desc=""/>
    <constraint field="psc" exp="" desc=""/>
    <constraint field="stavebniobjektkod" exp="" desc=""/>
    <constraint field="ulicekod" exp="" desc=""/>
    <constraint field="platiod" exp="" desc=""/>
    <constraint field="platido" exp="" desc=""/>
    <constraint field="idtransakce" exp="" desc=""/>
    <constraint field="globalniidnavrhuzmeny" exp="" desc=""/>
    <constraint field="isknbudovaid" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="1" sortExpression="&quot;cisloorientacni&quot;">
    <columns>
      <column type="field" width="-1" hidden="0" name="ogc_fid"/>
      <column type="field" width="-1" hidden="0" name="gml_id"/>
      <column type="field" width="-1" hidden="0" name="kod"/>
      <column type="field" width="-1" hidden="0" name="nespravny"/>
      <column type="field" width="-1" hidden="0" name="cislodomovni"/>
      <column type="field" width="167" hidden="0" name="cisloorientacni"/>
      <column type="field" width="-1" hidden="0" name="cisloorientacnipismeno"/>
      <column type="field" width="-1" hidden="0" name="psc"/>
      <column type="field" width="-1" hidden="0" name="stavebniobjektkod"/>
      <column type="field" width="-1" hidden="0" name="ulicekod"/>
      <column type="field" width="-1" hidden="0" name="platiod"/>
      <column type="field" width="-1" hidden="0" name="platido"/>
      <column type="field" width="-1" hidden="0" name="idtransakce"/>
      <column type="field" width="-1" hidden="0" name="globalniidnavrhuzmeny"/>
      <column type="field" width="-1" hidden="0" name="isknbudovaid"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="cislodomovni" editable="1"/>
    <field name="cisloorientacni" editable="1"/>
    <field name="cisloorientacnipismeno" editable="1"/>
    <field name="globalniidnavrhuzmeny" editable="1"/>
    <field name="gml_id" editable="1"/>
    <field name="idtransakce" editable="1"/>
    <field name="isknbudovaid" editable="1"/>
    <field name="kod" editable="1"/>
    <field name="nespravny" editable="1"/>
    <field name="ogc_fid" editable="1"/>
    <field name="platido" editable="1"/>
    <field name="platiod" editable="1"/>
    <field name="psc" editable="1"/>
    <field name="stavebniobjektkod" editable="1"/>
    <field name="ulicekod" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="cislodomovni"/>
    <field labelOnTop="0" name="cisloorientacni"/>
    <field labelOnTop="0" name="cisloorientacnipismeno"/>
    <field labelOnTop="0" name="globalniidnavrhuzmeny"/>
    <field labelOnTop="0" name="gml_id"/>
    <field labelOnTop="0" name="idtransakce"/>
    <field labelOnTop="0" name="isknbudovaid"/>
    <field labelOnTop="0" name="kod"/>
    <field labelOnTop="0" name="nespravny"/>
    <field labelOnTop="0" name="ogc_fid"/>
    <field labelOnTop="0" name="platido"/>
    <field labelOnTop="0" name="platiod"/>
    <field labelOnTop="0" name="psc"/>
    <field labelOnTop="0" name="stavebniobjektkod"/>
    <field labelOnTop="0" name="ulicekod"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>ogc_fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
