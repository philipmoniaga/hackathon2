
class FormatterOutput:
    @classmethod
    def output(cls, invitees):
        """
        Output to file output.txt with format
        """
        f = open('output.txt', 'w+')
        f.write("Result Invetees.\n\n")
        f.write("Id\t\tName\n")
        f.write("--------------\n")
        for invitee in invitees:
            user_id = str(invitee.user_id)
            f.write(user_id + "\t\t" + invitee.name + "\n")
        f.close()
