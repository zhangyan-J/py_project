import os
import logging
import zipfile
import log


def get_zip_dir(path):
    if os.path.exists('TargetPackage.zip'):
        os.remove('TargetPackage.zip')
    # try:
    #     zip = zipfile.ZipFile('TargetPackage.zip', "w", zipfile.ZIP_DEFLATED)
    #     for path, dirnames, filenames in os.walk(path):
    #         # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
    #         fpath = path.replace(path, '')
    #         for filename in filenames:
    #             zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    #     log.logger.info('flash_all_build: get_zip_dir: get TargetPackage.zip finished.')
    # except Exception as e:
    #     log.logger.error('flash_all_build: flash: failed reason is %s' % e.args)
    try:
        os.rename(path, os.path.join(os.getcwd(), "TargetPackage.zip"))
        log.logger.info('flash_all_build: get_zip_dir: get TargetPackage.zip finished.')
    except Exception as e:
        log.logger.error('flash_all_build: flash: failed reason is %s' % e.args)

get_zip_dir(r'D:\log')