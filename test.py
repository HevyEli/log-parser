import os
import sys
import logging
import datetime
from datetime import datetime
import shutil

def check_directory():
    logger.info(f"entering {check_directory.__name__}")
    logger.info(f"my current directory is: {my_dir}")
    logger.info(f"Required directory is: {required_dir} \n")
    if my_dir != required_dir:
        logger.info(f"your current directory is not {my_dir}. Required directory is: {required_dir} \n")
        logger.info(f"exiting...")
        sys.exit()
        return False
    elif my_dir == required_dir:
        logger.info(f"all OK, you are in right directory: {required_dir} \n")
        return True
    logger.info(f"exiting {check_directory.__name__}")
    return True

def read_file():
    logger.info(f"entering {read_file.__name__}")
    try:
        logger.info(f"reading file: {file_to_read} \n")
        
        """ check if output dir exists if not create directory"""
        dir_isExist = os.path.exists(output_files_directory)
        if dir_isExist != True:
            logger.info(f"Directory: {output_files_directory} does not exist, will be created")
            os.mkdir(output_files_directory)
        else: 
            logger.info(f"Directory {output_files_directory} exists")

        with open(file_to_read,mode='r') as input_file:
            with open(out_put_file,mode='a') as output_file:
                output_file.write(f"\ndate: {datetime} file name: {file_to_read}\n" + input_file.read()+ f"\nfile footer")
                logger.info(f"Data were successfully written into {out_put_file}")
        input_file.close()
       
        return True
    except Exception as e:
        logger.info.exception(e)
        return False
    logger.info(f"exiting {read_file.__name__}")

def create_files():
    logger.info(f"entering {create_files.__name__}")
    """ check if output dir exists if not create directory"""
    dir_isExist = os.path.exists(output_files_directory)
    if dir_isExist != True:
        logger.info(f"Directory: {output_files_directory} does not exist, will be created")
        os.mkdir(output_files_directory)
    else: 
        logger.info(f"Directory {output_files_directory} exists")

    with open(file_to_read,mode='r') as input_file:
        for index, line in enumerate(input_file):
                print(f"Line {index} : {line.strip()} - {line}") 
                with open(f"{output_files_directory}/{line.strip()}-{datetime}.txt", mode='w') as new_file:
                    logger.info(f"creating file: {line.strip()}-{datetime}.txt")
                    new_file.write(f"{line}")
        input_file.close()

    logger.info(f"exiting {create_files.__name__}")

def archive_file():
    logger.info(f"entering {archive_file.__name__}")
    """ check if archive dir exists if not create directory"""
    dir_isExist = os.path.exists(archive_directory)
    if dir_isExist != True:
        logger.info(f"Directory: {archive_directory} does not exist, will be created")
        os.mkdir(archive_directory)
    else: 
        logger.info(f"Directory {archive_directory} exists")
        shutil.copyfile(file_to_read, os.path.join(archive_directory + "/" + os.path.basename(file_to_read)))
        logger.info(f"file archived")
    logger.info(f"exiting {archive_file.__name__}")



my_dir = os.getcwd()
file_to_read = '/mnt/c/Users/eliasm1/Documents/learn//cities.txt'
out_put_file = '/mnt/c/Users/eliasm1/Documents/learn/python/output/output_python.txt'
required_dir = '/mnt/c/Users/eliasm1/Documents/learn/python'
current_time = datetime.now()
datetime = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
output_files_directory = '/mnt/c/Users/eliasm1/Documents/learn/python/output'
logfile = "/mnt/c/Users/eliasm1/Documents/learn/python/logs/output_python.txt"
archive_directory = '/mnt/c/Users/eliasm1/Documents/learn/python/archive'

logger = logging.basicConfig(level=logging.INFO, 
                    format='%(levelname)s: file name: %(filename)s.%(funcName)s: line %(lineno)d date: %(asctime)s: %(message)s',
                    handlers=[
                        logging.FileHandler(filename=logfile, mode="a"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(name='python')


if __name__ == '__main__':
    logger.info(f"program started at: {datetime}")
    check_directory()
    read_file()
    create_files()
    archive_file()
    logger.info(f"program finished at: {datetime}")

