import plotly.plotly as py      # Every function in this module will communicate with an external plotly server
py.plot({                      # use `py.iplot` inside the ipython notebook
"data": [{
    "x": [1, 2, 3],
    "y": [4, 2, 5]
}],
"layout": {
    "title": "hello world"
}
}, filename='hello world',      # name of the file as saved in your plotly account
sharing='public'