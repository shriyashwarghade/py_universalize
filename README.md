
# PyUniversalize
## The internationalization (i18n) library for Python.


### Installing
PyUniversalize can be installed with [pip](https://pip.pypa.io):

    pip install py_universalize
  
  Alternatively, you can grab the latest source code from [GitHub](https://github.com/shriyashwarghade/py_universalize):
  
	$ git clone https://github.com/shriyashwarghade/py_universalize
	$ cd py_universalize
	$ pip install .

 ### Importing Package

	import universalize
	
### Setting up PyUniversalize
Setup can be done 2 ways
 - Passing configuration as an parameter.
	``` python
	universalize.setup({  
		  "primary": {  
			  "code": "en",  
			  "file": "en.json",  
			  "display_name": "English"  
			  },  
		  "languages": [
				{  
			      "code": "fr",  
				  "file": "fr.json",  
				  "display_name": "French"  
				}  
			]  
		}
	)
	```
- Passing configuration as an Json file path.
	```python
	universalize.setup('setup.json')
	```

	```Json
	// setup.json
	{  "primary":  {  "code":  "en",  "file":  "en.json",  "display_name":  "English"  },  "languages":  [  {  "code":  "fr",  "file":  "fr.json",  "display_name":  "French"  }  ]  }
	```
Each language block has 3 keys. 
&nbsp;&nbsp;&nbsp;&nbsp;`code`: Language code,
&nbsp;&nbsp;&nbsp;&nbsp;`file`: Language translation json file location  
&nbsp;&nbsp;&nbsp;&nbsp;`display_name`:  Language display name

### Translate	
Once you've completed the setup, you can use locale function with the value by using the dot notation, ex:  `HOME.HELLO`.
The translate parser understands nested JSON objects. This means that you can have a translation that looks like this:
```Json
// fr.json
{
    "HOME": {
        "HELLO": "Hola"
    }
}
```

```python
universalize.locale('HOME.HELLO','fr')
```
`locale` function accepts  two parameters
&nbsp;&nbsp;&nbsp;&nbsp; `text`:  Dot notated string
&nbsp;&nbsp;&nbsp;&nbsp; `language_code`: Translate `text` to the given language code. This is an optional parameter. If not given `text` will be translated to primary language.

### Change Primary Language

```python
universalize.set_primary_language('en')
```

### Get Languages List	
Returns an array of currently available languages	

```python
 universalize.get_languages()
```

## License

MIT
