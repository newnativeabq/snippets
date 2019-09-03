from os import path
import wget
import logging

# Module logger
logging.getLogger(name='snippets.files')

def DownloadFile(url, name=None, target_dir=None):
    '''
    Check if file exists and download to working directory if it does not. Returns str of filename given to file.
        Arguments: url = str_of_fully_qualified_url, name=str_of_name_you_want
    '''

    # Function logger
    logger = logging.getLogger('snippets.files.DownloadFile')

    # Strip url for ending filename
    split_url = url_split = url.split('/')
    logger.info('Splitting URL into filename')
    if len(split_url) > 2:
        filename = url_split[len(url_split)-1]
    else:
        filename = url_split[1]
    logger.info('Filename returned as' + filename)

    # Check if target_dir parameter given.  If so, append to new filename.
    if not target_dir:
        logger.info('No directory given.  Setting taret_dir to empty')
        target_dir = ''
    else:
        if not path.isdir(target_dir):
            print('directory not found')
            return
    suffix = '.'.join(filename.split('.')[1:])

    # Check if name given
    if name:
        outpath = target_dir + name + '.' + suffix
    else:
        outpath = filename
    logger.info('Save path (outpath) created as' + outpath )

    if path.exists(outpath):
        print('File already exists')
        logger.info('File not saved. File already exists at ' + outpath)
    else:
        try:
            filename = wget.download(url, out=outpath)
            print(filename, 'successfully downloaded to' + outpath)
            logger.info('Download successful')
        except:
            print('File could not be downloaded.  Check URL & connection.')
            logger('Download failed. Except statement activated.')
    return filename


def UnzipFile(path, target_dir):
    '''
    Unpack compressed file to target directory.
        Arguments: path = str_of_path *relative or absolute, target_dir = str_of_path_to_dump
    '''
    from shutil import unpack_archive
    try:
        unpack_archive(path, target_dir)
    except:
        print('error unzipping')
    
