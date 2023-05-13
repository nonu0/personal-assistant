import webbrowser
chrome_path = "C:\\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

text = 'youtube.com'
webbrowser.open_new_tab(text)
print(text)