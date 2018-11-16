require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(arr, k) }

  describe "Test case #1" do
    let(:arr) { [2, 8, 7, 15, 19, 32, 6] }
    let(:k) { 4 }

    it { expect(subject.sort).to eq([2, 6, 7, 8]) }
  end

  describe "Test case #2" do
    let(:arr) { [1, 4, 67, 5, 3, 8, 2, 90] }
    let(:k) { 3 }

    it { expect(subject.sort).to eq([1, 2, 3]) }
  end

  describe "Test case #3" do
    let(:arr) { (1..100).to_a }
    let(:k) { 5 }

    it { expect(subject.sort).to eq([1, 2, 3, 4, 5]) }
  end

  describe "Test case #4" do
    let(:arr) { (1..100).to_a.shuffle }
    let(:k) { 30 }

    it { expect(subject.sort).to eq((1..30).to_a) }
  end

  describe "Test case #5" do
    let(:arr) { (1..5).to_a.shuffle }
    let(:k) { 5 }

    it { expect(subject.sort).to eq((1..5).to_a) }
  end

  describe "Test case #6" do
    let(:arr) { [] }
    let(:k) { 2 }

    it { is_expected.to be_empty }
  end
end
