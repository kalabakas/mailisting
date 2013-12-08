mailisting
==========

campaign monitor simple client
It s a python webapp powered by web.py microframework

Requirements
* web.py
* createsend

```
pip install web.py
pip install createsend
```

Create a "setting.py" as a copy from template.settings.py
```
cp template.setting.py settings.py
```
and set you API_KEY and the LIST_ID. Check [here](http://help.campaignmonitor.com/topic.aspx?t=206)
```
vim settings.py
```

You are ready to run the app,
```
python controller.py
```
If you see this 
```
"http://0.0.0.0:8080/"
```
you are ok!! 
