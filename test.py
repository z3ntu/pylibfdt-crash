#!/usr/bin/python3
# SPDX-License-Identifier: WTFPL

import libfdt


def fdt_for_each_subnode(fdt, nodeoffset):
    subnode_offset = fdt.first_subnode(nodeoffset)
    yield subnode_offset
    while True:
        try:
            subnode_offset = fdt.next_subnode(subnode_offset)
            yield subnode_offset
        except libfdt.FdtException:
            return


with open("kona-mtp.dtb", "rb") as f:
    fdt = libfdt.Fdt(f.read())

bus_node = fdt.path_offset('/soc/ad-hoc-bus')
for _ in range(0, 10):
    nodes = []

    for node in fdt_for_each_subnode(fdt, bus_node):
        try:
            fdt.getprop(node, "qcom,bcms")
        except libfdt.FdtException:
            pass
print("Done!")
