#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 13:15:32 2020

@author: wojciechprazuch
"""

import plotly.graph_objects as go

fig = go.Figure(
        data = go.Bar(y=[1, 2, 3]),
        layout_title_text = "Spyder Demo"
        )

fig.show()