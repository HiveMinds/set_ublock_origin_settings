"""Gets a website controller and opens it."""
from selenium import webdriver

from .Hardcoded import Hardcoded


# pylint: disable=R0903
class Website_controller:
    """Controls/commands website using selenium."""

    def __init__(self):
        """Constructs object that controlls a firefox browser.

        TODO: Allow user to switch between running browser
        in background or foreground.
        """
        self.hardcoded = Hardcoded()
        # To run Firefox browser in foreground
        print("Loading geckodriver")
        # TODO: write a try catch, if it fails:
        # TODO: check if firefox is installed with snap.
        # TODO: if yes, ask user to uninstall and re-install with link.
        try:
            # TODO: get the profile automatically.

            self.driver = webdriver.Firefox(
                # executable_path=r"firefox_driver/geckodriver",capabilities=firefox_capabilities
                executable_path=r"firefox_driver/geckodriver",
                firefox_profile=self.hardcoded.firefox_profile,
            )
        # pylint: disable=W0707
        except:
            # pylint: disable=W0707
            raise Exception(
                "Error, you have the snap Firefox browser installed"
                + ". Please use the apt one instead. This switching is automated"
                + " in a bash script of the Self-host GitLab."
            )

        # To run Firefox browser in background
        # os.environ["MOZ_HEADLESS"] = "1"
        # self.driver = webdriver.Firefox(executable_path=r"firefox_driver/geckodriver")

        # To run Chrome browser in background
        # options = webdriver.ChromeOptions();
        # options.add_argument('headless');
        # options.add_argument('window-size=1200x600'); // optional
