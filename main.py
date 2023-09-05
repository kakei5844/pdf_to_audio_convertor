import argparse
import pyttsx3, PyPDF2

def valid_pdf(f):
    if f.endswith('.pdf'):
        return f
    else:
        raise argparse.ArgumentTypeError('not a PDF file.')


def toAudio(args):
    pdfreader = PyPDF2.PdfReader(open(args.file[0], 'rb'))
    speaker = pyttsx3.init()

    for page in pdfreader.pages:
        text = page.extract_text()
        speaker.say(text.strip().replace('\n',' '))
        speaker.runAndWait()

    speaker.stop()


def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "PDF to Audio Convertor")

    # defining arguments for parser object
    parser.add_argument("-f", "--file", type = valid_pdf, nargs = 1, required=True,
                        help = "It needs to be an PDF file. Input format: path/filename. Example: documents/book.pdf")
    
    # Parse the arguments from standard input
    args = parser.parse_args()
    
    toAudio(args)


main()