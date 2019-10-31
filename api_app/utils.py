import operator
import copy

def allocation_portions(ip_dict, operation, portions):
    operation_dict = {
        "-": operator.sub,
        "+": operator.add,
    }
    sum_of_ratios = sum([v for k, v in ip_dict.items()])
    if sum_of_ratios == portions:
        return ip_dict
    else:
        if operation == "-":
            for k in ip_dict.keys():
                if ip_dict[k] > 0:
                    op_func = operation_dict[operation]
                    ip_dict[k] = op_func(ip_dict[k], 1)
                    if sum([v for k, v in ip_dict.items()]) == portions:
                        break
                    else:
                        pass
                else:
                    pass
        elif operation == "+":
            set_of_values = set([v for v in ip_dict.values()])
            keys_to_update_for_this_value = max(set_of_values)
            op_func = operation_dict[operation]
            for k in ip_dict.keys():
                if ip_dict[k] == keys_to_update_for_this_value:
                    ip_dict[k] = op_func(ip_dict[k], 1)
                    if sum([v for k, v in ip_dict.items()]) == portions:
                        break
                    else:
                        pass

        return allocation_portions(ip_dict, operation, portions)


def distribute(ip_dict, portions):
    if len(ip_dict) == 0 : return ip_dict
    portions = int(portions)
    sum_of_ratios = sum([v for k, v in ip_dict.items()])
    if sum_of_ratios > portions:
        operation = '-'
        extra = sum_of_ratios - portions
        return allocation_portions(ip_dict, operation, portions)
    elif sum_of_ratios < portions:
        operation = '+'
        extra = portions - sum_of_ratios
        return allocation_portions(ip_dict, operation, portions)