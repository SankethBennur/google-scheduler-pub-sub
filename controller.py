import os
import json


class controller():
    def __init__(self, message):
        """
        """
        self.message = message
        self.shell_command = ""

        data = message.data.decode('utf-8')
        attributes = (dict(message.attributes))
        msg_dict = {"data":data, "attributes":attributes}

        if("Daily Report".lower() in data.lower()):
            self.shell_command = self.construct_shell_command(
                                    py_module="daily_reports.py",
                                    message_dict=msg_dict
                                )
        elif("Instagram Ad Post Insights".lower() in data.lower()):
            self.shell_command = self.construct_shell_command(
                                    py_module="instagram_ad_insights.py",
                                    message_dict=msg_dict
                                )


    def construct_shell_command(self, py_module, message_dict):
        """
        """
        shell_command = ""
        shell_command = "python {0} \"{1}\"".format(
                                            py_module,
                                            json.dumps(message_dict)\
                                                .replace('\"','\\"')
                                        )
        print("$>  {}".format(shell_command))
        return shell_command


    def exec(self):
        """
        """
        os.system(self.shell_command)

