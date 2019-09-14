import json


class Parser:

    @classmethod
    def parsing(cls, file_path, decoder):
        """
        Return list of data object
        Parsing Json from file path and decode using decoder
        """
        data = []
        with open(file_path) as f:
            for line in f:
                try:
                    obj = json.loads(line, cls=decoder)
                except Exception as e:
                    raise Exception('error in line %s' % line + e.message)
                data.append(obj)
        return data
