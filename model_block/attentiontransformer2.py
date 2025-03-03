# -*- coding: utf-8 -*-

import torch
from torch import nn
import torch.nn.functional as F

from asppddgl import *
from seblock import *


class AttentionTransformer(nn.Module):
    def __init__(self, in_channels=512):
        super(AttentionTransformer, self).__init__()
        self.aspp = ASPP(in_channel=in_channels)
        self.se = SEBlock(in_planes=in_channels // 2, planes=in_channels)

        # self.aspp = nn.Sequential()
        # self.se = SEBlock(in_planes=in_channels, planes=in_channels)

    def forward(self, x):
        feature = self.aspp(x)

        out = self.se(feature)

        return out
