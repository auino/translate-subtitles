import time
import argparse
import progressbar
import simplejson as json
from google_translator_simplified import Translator

# just to print additional information while processing data
DEBUG = False

# the size of the progress bar
PROGRESSBAR_SIZE = 100

# sleep for a certain period (API_SLEEP_TIME), in seconds, after a specific amount (API_SLEEP_COUNT) of elements processed, to bypass API limitations
API_SLEEP_COUNT = 10
API_SLEEP_TIME = 10

# splits text t according to the split in b
def split_text(t, b):
	r = []
	k = int(len(t)/len(b))
	i_start = 0
	i_end = k
	for i in range(0, len(b)):
		x = i_start + k
		try: i_end = x + t[x:].index(' ')
		except: i_end = len(t)
		v = t[i_start:i_end]
		r.append(v)
		i_start = i_end + 1
	return r

def translate_text(t, l_in, l_out):
	if type(t) == str: t = json.loads(t)
	v = Translator.get_translation(l_out, ' '.join(t), l_in)
	return split_text(v, t)

def process(input_file, input_language, output_file, output_language):
	# loading input file
	f = open(input_file, 'r')
	input_text = f.read()
	f.close()
	# producing the data structure used to extract results
	values = input_text.split('\n\n')
	bar = progressbar.ProgressBar(maxval=PROGRESSBAR_SIZE, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	if not DEBUG: bar.start()
	i = 0
	r = []
	for e in values:
		e = e.split('\n')
		if len(e) < 2: continue
		obj = {}
		obj['index'] = e[0]
		obj['timing'] = e[1]
		obj['text_original'] = e[2:]
		obj['text_translated'] = translate_text(obj.get('text_original'), input_language, output_language)
		r.append(obj)
		if DEBUG: print('{}: {}'.format(obj.get('index'), ' '.join(obj.get('text_translated'))))
		i += 1
		if not DEBUG: bar.update(int(i / len(values) * PROGRESSBAR_SIZE))
		if i % API_SLEEP_COUNT == 0: time.sleep(API_SLEEP_TIME)

	# producing the output text
	output = ''
	for obj in r:
		output += '{}\n{}\n{}\n\n'.format(obj.get('index'), obj.get('timing'), '\n'.join(obj.get('text_translated')))
	# saving the output file
	f = open(output_file, 'w')
	f.write(output)
	f.close()

	if not DEBUG: bar.finish()

# arguments parsing
parser = argparse.ArgumentParser(description='Translates srt subtitles files')
parser.add_argument('-i', type=str, dest="input_file", help='The input srt file', required=True)
parser.add_argument('-o', type=str, dest="output_file", help='The output srt file', required=True)
parser.add_argument('-il', type=str, dest="input_language", help='The input language (e.g. "en", "it", "es", "fr")', required=True)
parser.add_argument('-ol', type=str, dest="output_language", help='The output language (e.g. "en", "it", "es", "fr")', required=True)
args = parser.parse_args()

# running the main process
process(args.input_file, args.input_language, args.output_file, args.output_language)
