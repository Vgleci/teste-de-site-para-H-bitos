
class Habit:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.done = False

    def toggle(self):
        self.done = not self.done

    def __str__(self):
        status = "[X]" if self.done else "[ ]"
        return f"{status} {self.id}: {self.name}"

class HabitTracker:
    def __init__(self):
        self.habits = []
        self.next_id = 1

    def add_habit(self, name):
        if not name.strip():
            print("Nome do hábito não pode estar vazio.")
            return
        habit = Habit(self.next_id, name)
        self.habits.append(habit)
        self.next_id += 1

    def remove_habit(self, id):
        original_count = len(self.habits)
        self.habits = [h for h in self.habits if h.id != id]
        if len(self.habits) == original_count:
            print(f"Hábito com ID {id} não encontrado.")

    def toggle_habit(self, id):
        for h in self.habits:
            if h.id == id:
                h.toggle()
                return
        print(f"Hábito com ID {id} não encontrado.")

    def list_habits(self):
        if not self.habits:
            print("Nenhum hábito registrado.")
        else:
            for h in self.habits:
                print(h)

def main():
    tracker = HabitTracker()
    while True:
        print("\n=== Rastreador de Hábitos ===")
        print("1. Listar hábitos")
        print("2. Adicionar hábito")
        print("3. Alternar status do hábito")
        print("4. Remover hábito")
        print("5. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            tracker.list_habits()
        elif choice == '2':
            name = input("Nome do novo hábito: ").strip()
            tracker.add_habit(name)
        elif choice == '3':
            try:
                id = int(input("ID do hábito para alternar: "))
                tracker.toggle_habit(id)
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        elif choice == '4':
            try:
                id = int(input("ID do hábito para remover: "))
                tracker.remove_habit(id)
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == '__main__':
    main()
