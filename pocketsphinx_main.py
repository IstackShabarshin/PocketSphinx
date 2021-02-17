import os, time
from pocketsphinx import AudioFile, get_model_path

model_path = get_model_path()
exmpl_path = os.getcwd()
exmpl_path = os.path.join(exmpl_path, 'examples')

start = time.process_time()
print('start of init')
speech = AudioFile(
    verbose=False,
    audio_file=os.path.join(exmpl_path, 'coming_home_red_16000.raw'),
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'my_dict.dic')
    # dic=os.path.join(model_path, 'ru.dic')
)
stop = time.process_time()
print('time of init - ' + str(stop - start))

#digits_16000
start = time.process_time()
for _ in speech:
    pass
stop = time.process_time()
print('time of recognizing - ' + str(stop - start))
print(str(speech))

# #hello_world
# speech.audio_file=os.path.join(exmpl_path, 'hello_world_16000.raw')
# speech.f = open(speech.audio_file, 'rb') #это просто отвратительно
# start = time.process_time()
# for _ in speech:
#     pass
# stop = time.process_time()
# print('time of recognizing - ' + str(stop - start))
# print(str(speech))

# #close_file
# speech.audio_file=os.path.join(exmpl_path, 'close_file_16000.raw')
# speech.f = open(speech.audio_file, 'rb') #это просто отвратительно
# start = time.process_time()
# for _ in speech:
#     pass
# stop = time.process_time()
# print('time of recognizing - ' + str(stop - start))
# print(str(speech))