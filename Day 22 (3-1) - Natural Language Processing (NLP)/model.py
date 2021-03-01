import torch

class Model():
    def __init__(self):
        self.model = torch.hub.load('pytorch/fairseq', 'roberta.large')
        self.model.eval()

    def autocomplete(self, phrase: str, num: int) -> list:
        results = self.model.fill_mask(phrase + " <mask>", topk=num)
        return [result[0] for result in results]