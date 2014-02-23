# #!/usr/bin/python2
# # coding: utf-8

# from   binascii              import hexlify
# from   holypy.utils.iters    import split
# from   holypy.utils.prettify import prettify, RED
# from   holypy.utils.strings  import string_to_bytes

# ################################################################################
# ### Constants
# ################################################################################

# SIZE_32   = 4
# SIZE_64   = 8
# MODIFIERS = {
#   1: "hh",
#   2: "h",
#   4: "",
#   8: "l",
# }

# ################################################################################
# ### Methods
# ################################################################################

# def payload(addr, value, index, size = SIZE_32, chunk_size = 2, reverse = True, copy = False):
#     chunks  = create_chunks(addr, value, size, chunk_size, reverse)
#     counter = 0
#     payload = ""
#     for i, chunk in enumerate(chunks):
#         temp           = "".join(map(lambda x: chr(int(x, 16)), chunk["addr"]))
#         payload        += string_to_bytes(temp) if copy else temp
#         counter        += size
#         chunk["index"] = i
#     for i, chunk in enumerate(chunks):
#         addr_  = chunk["addr"]
#         value_ = chunk["value"]
#         index_ = chunk["index"]
#         offset = value_ - counter
#         if offset > 0:
#             payload += "%%%dc" % (offset)
#         elif offset < 0:
#             print prettify("[-] Format offset", RED)
#             return -1
#         payload += "%%%d$%sn" % (index + index_, MODIFIERS[chunk_size])
#         counter += offset
#     return payload


# def create_chunks(addr, value, size, chunk_size, reverse):
#     if isinstance(value, int):
#         length = size
#     addrs  = []
#     chunks = split_bytes(format_bytes(value, length, reverse), chunk_size, reverse)
#     for i, chunk in enumerate(chunks):
#         temp = addr + chunk_size * 2 * i
#         temp = split_bytes(format_bytes(temp, size, reverse), 1, reverse)
#         addrs.append({
#             "addr"  : temp,
#             "value" : int(chunk, 16),
#             "index" : -1
#         })
#     addrs.sort(key = lambda x: x["value"])
#     return addrs

# def format_bytes(value, size, reverse):
#     if isinstance(value, int):
#         value = "%x" % value
#     return value.rjust(size * 2, "0")

# def split_bytes(bytes_, size, reverse):
#     return endian(split(bytes_, size * 2), reverse)

# def endian(iter_, reverse):
#     return iter_[::-1] if reverse else iter_

# ################################################################################
# ### Module
# ################################################################################

# if __name__ == '__main__':
#     index   = 0
#     size    = SIZE_32
#     chunk   = 2
#     copy    = True
#     endian_ = False
#     print payload(0x41424344, 0x12345,   index, reverse = endian_, size = size, chunk_size = chunk, copy = copy)
#     print payload(0x4142434, 0x12345678, index, reverse = endian_, size = size, chunk_size = chunk, copy = copy)

print prettify("DO NOT USE THIS, USE THE ONE FROM THE PREVIOUS LIBRARY !", RED)
