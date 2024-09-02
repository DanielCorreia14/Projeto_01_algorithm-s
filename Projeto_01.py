import numpy as np
import time
import matplotlib.pyplot as plt
import zipfile
import os
import sys
import psutil
import platform
from datetime import datetime

sys.setrecursionlimit(10000)  # Aumenta o limite de recursão


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j], arr[i]

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j], arr[i]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort_iterative(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

# Funções para gerar vetores

def generate_random_array(n):
    return np.random.randint(0, n, size=n).tolist()

def generate_sorted_array(n):
    return list(range(n))

def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))

def save_array_to_file(directory, filename, arr):
    with open(os.path.join(directory, filename), 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return (time.time() - start_time) * 1000  # Retorna em milissegundos

# Função para processar os vetores

def process_array(n, output_dir):
    # Gerar vetores
    random_arr = generate_random_array(n)
    sorted_arr = generate_sorted_array(n)
    reverse_sorted_arr = generate_reverse_sorted_array(n)

    # Salvar vetores
    save_array_to_file(output_dir, f"array_{n}_aleatorio_pre_ord.txt", random_arr)
    save_array_to_file(output_dir, f"array_{n}_crescente_pre_ord.txt", sorted_arr)
    save_array_to_file(output_dir, f"array_{n}_decrescente_pre_ord.txt", reverse_sorted_arr)

    print(f"Vetores de tamanho {n} salvos.")
    print(f"- Vetor Aleatório de tamanho {n} salvo como 'array_{n}_aleatorio_pre_ord.txt'.")
    print(f"- Vetor Ordenado Crescente de tamanho {n} salvo como 'array_{n}_crescente_pre_ord.txt'.")
    print(f"- Vetor Ordenado Decrescente de tamanho {n} salvo como 'array_{n}_decrescente_pre_ord.txt'.")

    # Medir tempos de execução
    times = {
        'Bubble Sort Random': measure_time(bubble_sort, random_arr),
        'Bubble Sort Cresc': measure_time(bubble_sort, sorted_arr),
        'Bubble Sort Desc': measure_time(bubble_sort, reverse_sorted_arr),
        'Bubble Sort Optimized Random': measure_time(bubble_sort_optimized, random_arr),
        'Bubble Sort Optimized Cresc': measure_time(bubble_sort_optimized, sorted_arr),
        'Bubble Sort Optimized Desc': measure_time(bubble_sort_optimized, reverse_sorted_arr),
        'Selection Sort Random': measure_time(selection_sort, random_arr),
        'Selection Sort Cresc': measure_time(selection_sort, sorted_arr),
        'Selection Sort Desc': measure_time(selection_sort, reverse_sorted_arr),
        'Insertion Sort Random': measure_time(insertion_sort, random_arr),
        'Insertion Sort Cresc': measure_time(insertion_sort, sorted_arr),
        'Insertion Sort Desc': measure_time(insertion_sort, reverse_sorted_arr),
        'Merge Sort Random': measure_time(merge_sort, random_arr),
        'Merge Sort Cresc': measure_time(merge_sort, sorted_arr),
        'Merge Sort Desc': measure_time(merge_sort, reverse_sorted_arr),
        'Quick Sort Random': measure_time(quick_sort_iterative, random_arr),
        'Quick Sort Cresc': measure_time(quick_sort_iterative, sorted_arr),
        'Quick Sort Desc': measure_time(quick_sort_iterative, reverse_sorted_arr),
    }

    # Exibir tempos
    for key, value in times.items():
        print(f"{key}: {value:.2f} ms")

    # Exportar tempos para arquivo
    with open(os.path.join(output_dir, f"tempos em ms_{n}.txt"), 'w') as file:
        for key, value in times.items():
            file.write(f"{key}: {value:.2f} ms\n")

    return times

def gather_system_info():
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    return {
        "Sistema": uname.system,
        "Nome do Host": uname.node,
        "Versão do Sistema": uname.version,
        "Processador": uname.processor,
        "Memória Total": f"{svmem.total / (1024 ** 3):.2f} GB",
        "Data e Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_report():
    # Diretório para salvar arquivos
    output_dir = "output_files"
    graph_dir = "graph_files"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(graph_dir, exist_ok=True)

    # Processar vetores e medir tempos
    sizes = [1000, 10000, 100000]
    results = {size: process_array(size, output_dir) for size in sizes}

    # Compactar arquivos em um ZIP
    with zipfile.ZipFile("output_files.zip", 'w') as zipf:
        for root, _, files in os.walk(output_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_dir))

    # Remover diretório de arquivos não compactados
    for root, _, files in os.walk(output_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        os.rmdir(root)

    # Recriar o diretório para salvar informações do sistema
    os.makedirs(output_dir, exist_ok=True)

    # Gerar gráficos
    for size in sizes:
        times = results[size]
        plt.figure(figsize=(12, 8))
        plt.bar(times.keys(), times.values())
        plt.xticks(rotation=90)
        plt.xlabel('Algoritmo e Tipo de Vetor')
        plt.ylabel('Tempo (milissegundos)')
        plt.title(f'Tempos de Execução para Vetores de Tamanho {size}')
        plt.tight_layout()
        plt.savefig(os.path.join(graph_dir, f"report_{size}.png"))
        plt.close()

    # Informações do sistema
    sys_info = gather_system_info()
    with open(os.path.join(output_dir, 'system_info.txt'), 'w') as file:
        for key, value in sys_info.items():
            file.write(f"{key}: {value}\n")

    print("Relatórios gerados e arquivos compactados com sucesso.")

if __name__ == "__main__":
    generate_report()

    print("Pressione Enter para sair...")
    input()  


"""
Método:
- Equipamento: Computador com :
Processador	13th Gen Intel(R) Core(TM) i7-13650HX   2.60 GHz
RAM instalada	16,0 GB (utilizável: 15,7 GB)
Tipo de sistema	Sistema operacional de 64 bits, processador baseado em x64

- Massa de Dados: Vetores de tamanhos 1.000, 10.000 e 100.000
- Algoritmos Utilizados: Bubble Sort, Bubble Sort Optimized, Selection Sort, Insertion Sort, Merge Sort, Quick Sort
- Linguagem de Programação: Python 3.x
- Bibliotecas Utilizadas: numpy para geração de vetores, matplotlib para gráficos

Descrição dos Métodos:
1. Bubble Sort: Algoritmo de ordenação simples baseado em comparação e troca de elementos adjacentes.
2. Bubble Sort Optimized: Versão otimizada do Bubble Sort que encerra a ordenação se não houver trocas.
3. Selection Sort: Algoritmo que seleciona o menor elemento e o coloca na posição correta.
4. Insertion Sort: Ordena inserindo elementos na posição correta em uma sublista já ordenada.
5. Merge Sort: Algoritmo de ordenação por divisão e conquista, que divide o vetor e faz a mesclagem.
6. Quick Sort: Algoritmo de ordenação por divisão e conquista que utiliza um pivô para particionar o vetor.

Gráficos e Análise:
- Gráficos comparando tempos de execução dos algoritmos para diferentes tamanhos de vetores serão gerados e salvos como sort_comparison.png.
- A análise crítica dos algoritmos e a comparação com a complexidade assintótica serão discutidas no relatório final.
"""
