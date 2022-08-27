import pyperclip
import re


def to_markdown(video_id: str) -> str:
    return f'[![](https://img.youtube.com/vi/{video_id}/mqdefault.jpg)](https://youtu.be/{video_id} "")'

def copy_and_display(strng):
    pyperclip.copy(strng)
    print(f'`{strng}` \nAlready copied to the clipboard!')
    

if __name__ == '__main__':
    buffer_url = pyperclip.paste()

    yurl_reg = re.compile(r"(https://)*(www\.)*(youtu\.be/|youtube\.com/watch\?v=)([A-z0-9]+)([\?\&].+)*")
    match = yurl_reg.match(buffer_url)

    if match:
        copy_and_display(to_markdown(match.group(4)))
    else:
        url = input('URL: ')
        match = yurl_reg.match(url)

        if match:
            copy_and_display(to_markdown(match.group(4)))
        else:
            print('Invalid URL!')
            
input()
