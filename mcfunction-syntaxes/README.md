# Custom mcfunction syntaxes

Here, I've compiled a list of some syntax tinkering I've done. There are just tweaks and conversions to existing, *amazing*, grammars out there.

Particularly, [language-mcfunction](https://github.com/Arcensoth/language-mcfunction) from Arcensoth is an amazing grammar for mcfunction highlighting.

I also extended this cool [Markdown Extended](https://github.com/jonschlinkert/sublime-markdown-extended) grammar for another syntax.

# Syntaxes:
- mcfunction-jinja
	- [Sublime](mcfunction-jinja.sublime-syntax) (Requires [Arc's Sublime](mcfunction.sublime-syntax) in User folder and [BetterJinja](https://github.com/Sublime-Instincts/BetterJinja))
	- [Textmate](mcfunction-jinja.YAML-tmLanguage) (Requires Arc's language somewhere (as `scope.mcfunction`) and Jinja2 extension as `text.jinja`)

- markdown-extended with mcfunction
	- [Sublime](Markdown Extended.sublime-syntax) (Requires [Arc's Sublime](mcfunction.sublime-syntax) in User folder)
	- [Textmate](Markdown Extended.YAML-tmLanguage) (Requires Arc's language somewhere (as `scope.mcfunction`))
