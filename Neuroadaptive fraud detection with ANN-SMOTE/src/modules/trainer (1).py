# Auto-generated Training Module
import torch

def train_step(model, loader, opt, crit, ewc_loss_fn=None):
    model.train()
    total_loss = 0
    for x, y in loader:
        opt.zero_grad()
        out = model(x)
        loss = crit(out, y)
        if ewc_loss_fn: loss += ewc_loss_fn(model)
        loss.backward()
        opt.step()
        total_loss += loss.item()
    return total_loss / len(loader)