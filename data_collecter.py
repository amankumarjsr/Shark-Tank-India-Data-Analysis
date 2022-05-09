class data_func:
    def each_episode_deal(self, episodes, deals):
        output = []
        count = 1
        temp = []
        for episode, deal in zip(episodes, deals):
            if episode == count:
                temp.append(deal)
            else:
                output.append(round(sum(temp), 2))
                temp = []
                temp.append(deal)
                count += 1
        output.append(
            sum([40, 0, 0])
        )  # since last iteration was not going to else block it was not appending
        return output

    def total_investment(self, data, individual_investment):
        output = []
        for item in data:
            temp = []
            index = 0
            for data in item:
                if data == 1:
                    temp.append(round(individual_investment[index], 2))
                    index += 1
                else:
                    index += 1
            output.append(sum(temp))
        return output
