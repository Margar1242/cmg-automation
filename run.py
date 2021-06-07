from multiprocessing import Pool

from appium.webdriver.appium_service import AppiumService

from runner_util.runner_helpers import *

if __name__ == '__main__':
    arguments = ArgParser().get_args()
    os.environ[URL] = arguments.env
    os.environ[RUN_MODE] = arguments.run_mode
    os.environ[HEADLESS] = str(arguments.headless)
    if arguments.headless:
        os.environ[DIMENSIONS] = arguments.dimensions

    if arguments.throughput is not None:
        os.environ[THROUGHPUT] = arguments.throughput
    if Types.MOBILE.value in arguments.type:
        generate_device_config_file(arguments)
        appium_service = AppiumService()
        appium_service.start()
    pool = Pool()
    if len(arguments.type) > 1:
        pool.map(run_command, arguments.type)
    else:
        pool.map(run_command, arguments.browser)
    pool.close()
    pool.join()
    if Types.MOBILE.value in arguments.type:
        appium_service.stop()
    generate_reports(arguments)
