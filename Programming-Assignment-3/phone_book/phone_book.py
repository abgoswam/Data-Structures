# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

    def __str__(self):
        return "{0}:{1}".format(self.type, self.number)


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries_fast(queries):
    result = []
    phonebook = {}
    for cur_query in queries:
        # print(cur_query)

        if cur_query.type == 'add':
            phonebook[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            phonebook.pop(cur_query.number, None)
        else:
            # has to be a find query
            if cur_query.number in phonebook:
                result.append(phonebook[cur_query.number])
            else:
                result.append("not found")

    return result


if __name__ == '__main__':
    write_responses(process_queries_fast(read_queries()))
