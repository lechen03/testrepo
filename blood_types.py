# Name: Le Chen
# Student ID: 261038117


# Write function below including a docstring
def is_compatible(donor, recipient):
    '''
    Evalute whether donor blood type is compatible
    with recipient blood type
    
    Args:
        donor: donor blood type
        recipient: recipient blood type
        
    Returns: True if donor blood type is compatible
             with recipient blood type
    '''
    
    # Assign 4 variables
    donor_anti = donor[:len(donor) - 1]
    reci_anti = recipient[:len(recipient) - 1]
    donor_rhes = donor[len(donor) - 1]
    reci_rhes = recipient[len(recipient) - 1]
    
    # Evalute compatibility of antigen
    if donor_anti == reci_anti:
        
        # Evaluate compatibility of rhesus
        if donor_rhes == "+" and reci_rhes == "-":
            return False
        else:
            return True

    elif donor_anti != reci_anti:
        
        # Evalute the two exceptions
        if donor_anti == "O" or reci_anti == "AB":
            if donor_rhes == "+" and reci_rhes == "-":
                return False
            else:
                return True 
        else:
            return False
        

# Test cases:
print(is_compatible("O+", "AB-"))  # False
print(is_compatible("O+", "A+"))  # True
print(is_compatible("A-", "AB-"))  # True
