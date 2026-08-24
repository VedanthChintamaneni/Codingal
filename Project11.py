def shutdown():
  answer = input("Do you want to shut down? (Yes/No): ").strip().lower()
  if answer == 'yes':
    print('Goodbye')
  else:
    print('Shutdown cancelled')


if __name__ == '__main__':
  shutdown()