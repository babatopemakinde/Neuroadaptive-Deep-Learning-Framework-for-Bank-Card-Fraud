# Auto-generated Evaluation Module
import torch
from sklearn.metrics import f1_score

def evaluate(model, loader, crit):
    model.eval()
    total_loss, all_preds, all_labels = 0, [], []
    with torch.no_grad():
        for x, y in loader:
            out = model(x)
            total_loss += crit(out, y).item()
            all_preds.extend((torch.sigmoid(out) > 0.5).float().cpu().numpy())
            all_labels.extend(y.cpu().numpy())
    return total_loss / len(loader), f1_score(all_labels, all_preds)