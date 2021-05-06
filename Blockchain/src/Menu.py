from Blockchain.src.Blockchain import Blockchain
import os


class Menu:
    def use_blockchain(self):
        blockchain = Blockchain()
        flag = 0
        while True:
            os.system('cls')
            self.show_menu()
            flag = input()
            print('you\'ve chosen ', flag)
            if flag == '1':
                print(blockchain.chain)

            elif flag == '2':
                sender = input('Enter sender')
                recipient = input('Enter recipient')
                amount = input('Enter amount')
                blockchain.new_transaction(sender, recipient, amount)
                print('transaction added')
            elif flag == '3':
                proof = input("Enter proof")
                blockchain.new_block(proof)
                print('block added')
            elif flag == '4':
                print('Number of blocks in chain:', len(blockchain.chain))
            elif flag == '5':
                index = int(input('enter index'))
                print('Block in the blockhain described by index', index)
                print(blockchain.chain[index - 1])
            elif flag == '6':
                break
            else:
                print('smth went wrong, choose your option again')
                self.show_menu()

    def show_menu(self):
        print('Tell me what you want to do')
        print('Enter 1 to show current state of blockchain')
        print('Enter 2 to add transaction')
        print('Enter 3 to commit a block')
        print('Enter 4 to display number of blocks in chain')
        print('Enter 5 to display given block')
        print('Enter 6 to end program')
