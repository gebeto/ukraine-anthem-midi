import mido
import os

files_mid = []
files_txt = []

for file in os.listdir():
    if file.endswith('.mid'):
        files_mid.append(mido.MidiFile(file))
        files_txt.append(open(file.split('.')[0]+'.txt','w'))

for i,file in enumerate(files_mid):
    output = ''
    for track in file.tracks:
        for msg in track:
            if msg.type == 'note_on':
                hex_note = hex(msg.note).split("0x")[1]
                # output += str(msg.note) + ','
                print(msg.note, hex_note)
                output += str(hex_note) + ','
    files_txt[i].write(output[:-1])
    files_txt[i].close()