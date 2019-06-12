# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-05-03 10:34
from __future__ import unicode_literals

from django.db import migrations
import json

def move_baselayers_to_layers(apps, schema_editor):
    try:
        BaseLayer = apps.get_model("gvsigol_core", "BaseLayer")
        Layer = apps.get_model("gvsigol_services", "Layer")
        LayerGroup = apps.get_model("gvsigol_services", "LayerGroup")
        Server = apps.get_model("gvsigol_services", "Server")
        
        default_server = Server.objects.get(default=True)
        default_baselayer_group = LayerGroup(
            server_id = default_server.id,
            name = '__default_baselayergroup__', 
            title = 'Base', 
            visible = False,
            cached = False,
            created_by = 'From migration'
        )
        default_baselayer_group.save()
        
        for bl in BaseLayer.objects.all():
            external_params = json.loads(bl.type_params)
            if bl.type == 'WMTS' or bl.type == 'WMS':
                external_params['alternative_url'] = external_params['url']

            external_layer = Layer(
                external = True,
                title = bl.title,
                layer_group = default_baselayer_group,
                type = bl.type,
                visible = False,
                queryable = False,
                cached = False,
                single_image = False,
                time_enabled = False,
                created_by = 'From migration',
                external_params = json.dumps(external_params)
            )
            external_layer.save()
            external_layer.name = 'externallayer_' + str(bl.id)
            external_layer.save()
            
    except Exception as error:
        print error
        

class Migration(migrations.Migration):

    dependencies = [
         ('gvsigol_services', '0020_auto_20190527_1633'),
         ('gvsigol_core', '0013_projectlayergroup_default_baselayer'),
    ]

    operations = [
        migrations.RunPython(move_baselayers_to_layers, reverse_code=migrations.RunPython.noop),
    ]
