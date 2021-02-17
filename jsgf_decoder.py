from os import environ, path, getcwd
from sys import stdout

from pocketsphinx import *
from sphinxbase import *

MODELDIR = get_model_path()
DATADIR = getcwd()
EXAMDIR = path.join(DATADIR, 'examples')

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'zero_ru.cd_cont_4000'))
# config.set_string('-lm', path.join(MODELDIR, 'ru.lm'))
config.set_string('-fsg',path.join(MODELDIR, 'goforward.fsg'))
config.set_string('-dict', path.join(MODELDIR, 'my_dictionary_out.dic'))
# config.set_string('-jsgf', path.join(DATADIR, 'gram.gram'))
config.set_string('-logfn', 'nul')
decoder = Decoder(config)

# # Decode with lm
# decoder.start_utt()
# stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
# while True:
#     buf = stream.read(1024)
#     if buf:
#          decoder.process_raw(buf, False, False)
#     else:
#          break
# decoder.end_utt()
# print ('Decoding with "turtle" language:', decoder.hyp().hypstr)

# Switch to JSGF grammar
# jsgf = Jsgf(path.join(MODELDIR, 'goforward.gram'))
# rule = jsgf.get_rule('goforward.move2')
# fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
# fsg.writefile('goforward.fsg')

# decoder.set_fsg('goforward.fsg', fsg)
# decoder.set_search("goforward")
# decoder.set_jsgf_file('gram',path.join(MODELDIR, 'gram.gram'))

decoder.start_utt()
stream = open(path.join(EXAMDIR, 'digits_16000.raw'), 'rb')
while True:
    buf = stream.read(1024)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
decoder.end_utt()
print ('Decoding with "goforward" grammar:', decoder.hyp().hypstr)